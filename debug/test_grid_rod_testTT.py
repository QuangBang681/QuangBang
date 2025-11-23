import numpy as np
import time

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

def test_grid_rod_testTT():
    # THỜI GIAN MÔ PHỎNG
    tsim = 20e-6

    # THÔNG SỐ ĐẤT
    res = 1000.0
    eps = 9.0
    depth = 0.8

    # KÍCH THƯỚC LƯỚI
    d_x = np.array([2, 4, 5.5, 5.5, 6, 8, 7, 7, 10.5, 6, 3.5], dtype=float)
    d_y = np.array([2.5, 5, 5, 7, 5, 5, 5.5, 5.5, 3.5, 3], dtype=float)
    rx = 0.007 * np.ones((len(d_y) + 1, len(d_x)))
    ry = 0.007 * np.ones((len(d_x) + 1, len(d_y)))
    re = 0.25e-6

    # CỌC (rod) theo trục z: ở script này thực tế set về 0
    p_z = np.zeros((len(d_x) + 1) * (len(d_y) + 1))
    rz = 0.015 * np.ones_like(p_z)

    # DÒNG SÉT VÀ VỊ TRÍ TÁC ĐỘNG
    def is_func(t):
        return 12500.0 * (np.exp(-190099.0 * t) - np.exp(-2922879.0 * t))

    Imsc = np.zeros_like(p_z)
    Imsc[0] = 1.0  # vị trí nút nhận dòng sét

    # TÍNH VỊ TRÍ VÀ HƯỚNG CÁC ĐOẠN
    x, y, z, r, d = locating_segments_position(d_x, d_y, p_z, rx, ry, rz)

    # XÁC ĐỊNH LIÊN KẾT NÚT-PHẦN TỬ
    node, element = determinating_junction(d_x, d_y, p_z)

    # TÍNH MA TRẬN THAM SỐ PUL R, P, L
    R, P, L = pul_parameter_matrixes(x, y, z, r, d, depth, res, eps)

    # RỜI RẠC THỜI GIAN
    dt = 1.0 / (3e8)
    Nt = int(round(tsim / dt))
    tv = np.arange(Nt + 1) * dt

    # THÔNG SỐ MÔ HÌNH ĐƠN GIẢN
    Ne = len(r)
    Rs = re / (np.pi * r**2)
    Ls = np.zeros(Ne)
    Gs = np.zeros(Ne)
    Cs = np.zeros(Ne)
    for i in range(Ne):
        Ls[i] = L[i, i]
        Gs[i] = 1.0 / R[i, i]
        Cs[i] = 1.0 / P[i, i]

    # ÁNH XẠ THÔNG SỐ VẬT LIỆU SANG MÔ HÌNH PHỨC TẠP
    Rc = simple2complex(d_x, d_y, p_z, Rs)

    # KHỞI TẠO DÒNG VÀ ÁP THEO THỜI GIAN
    iv, uv, dx = making_initial_value(Nt, d_x, d_y, p_z)
    V = np.zeros((len(d_x) + 1) * (len(d_y) + 1))

    Gob = np.zeros(Nt)
    Lob = np.zeros(Nt)
    Cob = np.zeros(Nt)

    start = time.time()
    for t in range(Nt):
        # Dòng sét tại thời điểm hiện tại
        Ims = Imsc * is_func(tv[t + 1])

        # Chuyển đổi sang mô hình đơn giản
        Is = complex2simple_current(d_x, d_y, p_z, iv, t)
        Vs = complex2simple_voltage(d_x, d_y, p_z, uv, t)

        # HỆ SỐ GHÉP GIỮA CÁC PHẦN ĐOẠN
        Aj_i, Bj_i, Dj_i = generally_coupling_coefficients_evaluating(Is, Vs, Gs, Cs)

        # CẬP NHẬT THAM SỐ PUL THEO THỜI GIAN TRONG MÔ HÌNH ĐƠN GIẢN
        Gs, Cs, Ls = per_unit_length_parameter_evaluating_at_each_time_step(Aj_i, Bj_i, Dj_i, R, P, L)
        Gob[t] = Gs[0]
        Lob[t] = Ls[0]
        Cob[t] = Cs[0]

        # ÁNH XẠ LẠI SANG MÔ HÌNH PHỨC TẠP
        Lc = simple2complex(d_x, d_y, p_z, Ls)
        Gc = simple2complex(d_x, d_y, p_z, Gs)
        Cc = simple2complex(d_x, d_y, p_z, Cs)

        # CẬP NHẬT DÒNG THEO THỜI GIAN
        iv = current_evaluating_at_each_time_step(iv, uv, Rc, Lc, t + 1, dx, dt)

        # CẬP NHẬT ÁP NÚT LƯỚI
        V = grid_junction_volage_evaluating(V, node, iv, uv, t + 1, Gc, Cc, Ims, dx, dt)

        # CẬP NHẬT ĐIỆN ÁP BIÊN PHẦN TỬ
        uv = voltage_evaluating_at_each_time_step(iv, uv, V, element, Gc, Cc, t + 1, dx, dt)

        # Tiến độ (10 bước một lần)
        if Nt >= 10 and t % (Nt // 10) == 0:
            print(f"Progress: {round(t / Nt * 100)}%")

    elapsed = time.time() - start
    print(f"Time to simulate: {elapsed:.2f} s")

    return tv, uv
