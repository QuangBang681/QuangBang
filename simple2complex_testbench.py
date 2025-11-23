import numpy as np
from simple2complex import simple2complex

def main():
    # Ví dụ: lưới 1x1, không có cọc
    d_x = np.array([10.0])
    d_y = np.array([10.0])
    p_z = np.zeros((len(d_x)+1)*(len(d_y)+1))

    Nx = len(d_x)
    Ny = len(d_y)
    Nxs = int(np.sum(np.ceil(d_x)))
    Nys = int(np.sum(np.ceil(d_y)))
    Ns = (Ny+1)*Nxs + (Nx+1)*Nys  # không có cọc

    # Tạo Xs giả định: vector từ 1..Ns
    Xs = np.arange(1, Ns+1)

    Xc = simple2complex(d_x, d_y, p_z, Xs)

    print("=== Testbench simple2complex ===")
    print(f"d_x={d_x}, d_y={d_y}, Ns={Ns}")
    print("Xs:", Xs)
    print("Xc (per element):")
    for idx, cell in enumerate(Xc, start=1):
        print(f" Element {idx}: {cell}")

if __name__ == "__main__":
    main()
