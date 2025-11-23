# making_initial_value_testbench.py
import numpy as np
from making_initial_value import making_initial_value

def main():
    # Grid: Nx=2, Ny=2
    d_x = [1.0, 0.6]
    d_y = [0.8, 1.2]
    Nx, Ny = len(d_x), len(d_y)
    Nju = (Nx + 1) * (Ny + 1)

    # Place rods at nodes 5 and 9 (1-based)
    p_z = np.zeros(Nju)
    p_z[5 - 1] = 0.75
    p_z[9 - 1] = 0.5

    Nt = 10  # 11 time points

    iv, uv, dx = making_initial_value(Nt, d_x, d_y, p_z)
    Nsum = len(iv)

    print("=== making_initial_value testbench ===")
    print(f"Nx={Nx}, Ny={Ny}, Nju={Nju}, Nt={Nt}")
    print(f"Nsum (elements) = {Nsum}")
    print(f"dx length = {dx.shape[0]}")
    print("\nFirst 6 elements summary:")
    for n in range(min(6, Nsum)):
        iv_shape = iv[n].shape if iv[n] is not None else None
        uv_shape = uv[n].shape if uv[n] is not None else None
        print(f"  n={n+1:2d}: iv.shape={iv_shape}, uv.shape={uv_shape}, dx={dx[n]:.4f}")

    # Verify blocks sizes
    expected_x = (Ny + 1) * int(np.sum(np.ceil(d_x)))
    expected_y = (Nx + 1) * int(np.sum(np.ceil(d_y)))
    expected_z = int(np.sum(np.ceil(p_z)))
    print(f"\nExpected block sizes -> X: {expected_x}, Y: {expected_y}, Z: {expected_z}")
    print(f"Total by formula: {expected_x + expected_y + expected_z}")

    # Check a rod element allocation (last elements)
    print("\nRod elements (end of list):")
    start_z = 2 * Nx * Ny + Nx + Ny  # 1-based start index of Z block
    for k in range(expected_z):
        n = start_z + k  # 1-based
        idx = n - 1
        print(f"  rod k={k+1}: element n={n}, iv.shape={iv[idx].shape}, uv.shape={uv[idx].shape}, dx={dx[idx]:.4f}")

if __name__ == "__main__":
    main()
