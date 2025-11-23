import numpy as np
import time
import matplotlib.pyplot as plt

# Import các hàm phụ từ file Python cùng tên
from locating_segments_position import locating_segments_position
from determinating_junction import determinating_junction
from pul_parameter_matrixes import pul_parameter_matrixes
from simple2complex import simple2complex
from making_initial_value import making_initial_value
from complex2simple_current import complex2simple_current
from complex2simple_voltage import complex2simple_voltage
from generally_coupling_coefficients_evaluating import generally_coupling_coefficients_evaluating
from per_unit_length_parameter_evaluating_at_each_time_step import per_unit_length_parameter_evaluating_at_each_time_step
from current_evaluating_at_each_time_step import current_evaluating_at_each_time_step
from grid_junction_volage_evaluating import grid_junction_volage_evaluating
from voltage_evaluating_at_each_time_step import voltage_evaluating_at_each_time_step
from expand_to_segments import expand_to_segments

def test_grid_rod():
    # NHẬP THỜI GIAN MÔ PHỎNG
    tsim = 20e-6

    # THÔNG SỐ CỦA ĐẤT
    res = 1000.0
    eps = 9.0

    # KÍCH THƯỚC LƯỚI (1x1 ô)
    depth = 0.5
    d_x = np.ones(1) * 10.0
    d_y = np.ones(1) * 10.0
    rx = 0.007 * np.ones((len(d_y) + 1, len(d_x)))
    ry = 0.007 * np.ones((len(d_x) + 1, len(d_y)))
    re = 0.25e-6

    # Cọc (rod) theo trục z: khởi tạo rồi set về 0 (không có cọc thực tế)
    p_z = np.zeros((len(d_x) + 1) * (len(d_y) + 1))
    rz = 0.015 * np.ones_like(p_z)

    # Dòng sét
    def is_func(t):
        return 1.0 * (np.exp(-27e3 * t) - np.exp(-56e5 * t))

    # Vị trí tác động dòng sét
    Imsc = np.zeros_like(p_z)
    Imsc[0] = 1.0

    # TÍNH TOÁN VỊ TRÍ, HƯỚNG CÁC PHÂN ĐOẠN
    x, y, z, r, d = locating_segments_position(d_x, d_y, p_z, rx, ry, rz)

    # XÁC ĐỊNH QUAN HỆ NÚT-PHẦN TỬ
    node, element = determinating_junction(d_x, d_y, p_z)

    # TÍNH MA TRẬN THAM SỐ TRÊN ĐƠN VỊ DÀI R,P,L
    R, P, L = pul_parameter_matrixes(x, y, z, r, d, depth, res, eps)

    # RỜI RẠC THỜI GIAN
    dt = 1.0 / (3e8)
    Nt = int(round(tsim / dt))
    tv = np.arange(Nt + 1) * dt

    # KHỞI TẠO THÔNG SỐ MÔ HÌNH ĐƠN GIẢN
    Ne = len(r)
    Rs = re / (np.pi * r**2)
    Ls = np.zeros(Ne)
    Gs = np.zeros(Ne)
    Cs = np.zeros(Ne)
    for i in range(Ne):
        Ls[i] = L[i, i]
        Gs[i] = 1.0 / R[i, i]
        Cs[i] = 1.0 / P[i, i]

    # ÁNH XẠ RS SANG MÔ HÌNH PHỨC TẠP
    Rc = simple2complex(d_x, d_y, p_z, Rs)

    # KHỞI TẠO DÒNG, ÁP, BƯỚC KHÔNG GIAN
    iv, uv, dx = making_initial_value(Nt, d_x, d_y, p_z)
    V = np.zeros((len(d_x) + 1) * (len(d_y) + 1))

    Gob = np.zeros(Nt)
    Lob = np.zeros(Nt)
    Cob = np.zeros(Nt)

    start_time = time.time()
    for t in range(Nt):
        # Dòng sét tại thời điểm khảo sát
        Ims = Imsc * is_func(tv[t + 1])

        # Chuyển đổi từ mô hình phức tạp sang đơn giản
        Is = complex2simple_current(d_x, d_y, p_z, iv, t)
        Vs = complex2simple_voltage(d_x, d_y, p_z, uv, t)

        # Hệ số tương hô giữa các phần đoạn
        Aj_i, Bj_i, Dj_i = generally_coupling_coefficients_evaluating(Is, Vs, Gs, Cs)

        # Tham số PUL tại mỗi bước thời gian trong mô hình đơn giản
        Gs, Cs, Ls = per_unit_length_parameter_evaluating_at_each_time_step(Aj_i, Bj_i, Dj_i, R, P, L)
        Gob[t] = float(Gs[0,0])
        Lob[t] = float(Ls[0,0])
        Cob[t] = float(Cs[0,0])


        # Ánh xạ trở lại mô hình phức tạp
        Ls_segments = expand_to_segments(d_x, d_y, p_z, Ls)
        Lc = simple2complex(d_x, d_y, p_z, Ls_segments)
        Gs_segments = expand_to_segments(d_x, d_y, p_z, Gs)
        Gc = simple2complex(d_x, d_y, p_z, Gs_segments)
        Cs_segments = expand_to_segments(d_x, d_y, p_z, Cs)
        Cc = simple2complex(d_x, d_y, p_z, Cs_segments)

        # Lc = simple2complex(d_x, d_y, p_z, Ls)
        # Gc = simple2complex(d_x, d_y, p_z, Gs)
        # Cc = simple2complex(d_x, d_y, p_z, Cs)

        # Tính dòng ở bước thời gian
        iv = current_evaluating_at_each_time_step(iv, uv, Rc, Lc, t + 1, dx, dt)

        # Tính điện áp nút lưới ở bước thời gian
        V = grid_junction_volage_evaluating(V, node, iv, uv, t + 1, Gc, Cc, Ims, dx, dt)

        # Tính điện áp biên phần tử ở bước thời gian
        uv = voltage_evaluating_at_each_time_step(iv, uv, V, element, Gc, Cc, t + 1, dx, dt)

        # Tiến độ (in thưa để tránh spam)
        if Nt >= 10 and t % max(1, Nt // 10) == 0:
            print(f"Progress: {round(t / Nt * 100)}%")

    elapsed = time.time() - start_time
    print(f"Time to calculate current and voltage over time: {elapsed:.2f} s")

    # Vẽ tương tự MATLAB: plot(tv*10^6, uv{1}(:,1)')
    plt.figure(figsize=(8,5))
    plt.plot(tv * 1e6, uv[0][:, 0], label="U(V) at first element, left endpoint")
    plt.xlabel("t (µs)")
    plt.ylabel("U (V)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Lưu kết quả (tương đương save .mat): dùng npz
    # Bạn có thể chuyển sang scipy.io.savemat nếu muốn .mat
    np.savez("ket_qua_luoi_11RBF.npz", tv=tv, uv=uv)

    return tv, uv
