import numpy as np
from current_evaluating_at_each_time_step import current_evaluating_at_each_time_step

def build_dummy_data(N=2, T=5, seg_counts=[3,4]):
    """
    Tạo dữ liệu giả cho iv, uv, Rc, Lc.
    - iv: mỗi phần tử là ma trận (T x seg_count)
    - uv: mỗi phần tử là ma trận (T x (seg_count+1))
    """
    iv = []
    uv = []
    Rc = []
    Lc = []
    dx = []

    for i in range(N):
        seg_count = seg_counts[i]
        iv.append(np.random.rand(T, seg_count))
        uv.append(np.random.rand(T, seg_count+1))
        Rc.append(0.5 + 0.1*i)  # resistance
        Lc.append(1.0 + 0.2*i)  # inductance
        dx.append(1.0 + 0.5*i)  # length

    return iv, uv, Rc, Lc, dx

def main():
    # Tạo dữ liệu giả
    iv, uv, Rc, Lc, dx = build_dummy_data(N=2, T=6, seg_counts=[3,4])
    dt = 0.01
    t = 3  # cập nhật tại bước thời gian thứ 3

    print("=== Trước khi cập nhật ===")
    print("iv[0][t,:] =", iv[0][t,:])
    print("iv[1][t,:] =", iv[1][t,:])

    iv = current_evaluating_at_each_time_step(iv, uv, Rc, Lc, t, dx, dt)

    print("\n=== Sau khi cập nhật ===")
    print("iv[0][t,:] =", iv[0][t,:])
    print("iv[1][t,:] =", iv[1][t,:])

if __name__ == "__main__":
    main()
