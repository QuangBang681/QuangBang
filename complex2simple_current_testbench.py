import numpy as np
from complex2simple_current import complex2simple_current

def build_Ic(d_x, d_y, p_z, T=5):
    """
    Xây dựng dữ liệu giả cho Ic, đảm bảo số cột khớp với số đoạn (ceil).
    Mỗi phần tử Ic[nc] là ma trận (T x seg_count).
    """
    Nx = len(d_x)
    Ny = len(d_y)
    rod = [i for i, v in enumerate(p_z) if v != 0]
    Nz = len(rod)
    Ic = []

    # --- X-bars ---
    for j in range(Ny + 1):
        for i in range(Nx):
            seg_count = int(np.ceil(d_x[i]))
            arr = np.random.rand(T, seg_count)
            Ic.append(arr)

    # --- Y-bars ---
    for i in range(Nx + 1):
        for j in range(Ny):
            seg_count = int(np.ceil(d_y[j]))
            arr = np.random.rand(T, seg_count)
            Ic.append(arr)

    # --- Z-rods ---
    for k in range(Nz):
        seg_count = int(np.ceil(p_z[rod[k]]))
        arr = np.random.rand(T, seg_count)
        Ic.append(arr)

    return Ic

def main():
    # Ví dụ nhỏ
    d_x = [1.2, 2.7]   # 2 bars along x
    d_y = [1.5]        # 1 bar along y
    p_z = [0, 2.2]     # 1 rod along z (second entry nonzero)

    # Xây dựng dữ liệu Ic khớp với số đoạn
    Ic = build_Ic(d_x, d_y, p_z, T=10)

    # Chọn time index
    t = 2
    Is = complex2simple_current(d_x, d_y, p_z, Ic, t)

    print("=== Testbench Result ===")
    print("Output Is vector:", Is)
    print("Length of Is:", len(Is))

    # Kiểm tra độ dài mong đợi
    expected_length = (len(d_y)+1)*np.sum(np.ceil(d_x)) \
                      + (len(d_x)+1)*np.sum(np.ceil(d_y)) \
                      + np.sum(np.ceil(p_z))
    print("Expected length:", int(expected_length))

    if len(Is) == expected_length:
        print("✅ Length matches expected value.")
    else:
        print("❌ Length mismatch!")

if __name__ == "__main__":
    main()
