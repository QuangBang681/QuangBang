# QS_complex2simple_voltage_testbench.py
import numpy as np
from QS_complex2simple_voltage import QS_complex2simple_voltage

def main():
    # Grid: Nx=2, Ny=2
    d_x = [1.0, 0.6]
    d_y = [0.8, 1.2]
    Nx, Ny = len(d_x), len(d_y)
    Nxs = int(np.sum(np.ceil(d_x)))    # segments per row along x
    Nys = int(np.sum(np.ceil(d_y)))    # segments per column along y
    Ns = (Ny + 1) * Nxs + (Nx + 1) * Nys

    # Build uv list (X elements then Y elements), without Z elements
    Nt = 5  # Nt+1 time samples
    uv = []

    # X block: elements n = i + (j-1)*Nx for j=1..Ny+1, i=1..Nx
    for j in range(1, Ny + 2):
        for i in range(1, Nx + 1):
            Nxi = int(np.ceil(d_x[i - 1]))
            # Create uv entry: (Nt+1, Nxi+1)
            # Fill with simple pattern for verification
            arr = np.zeros((Nt + 1, Nxi + 1), dtype=float)
            for t in range(Nt + 1):
                arr[t, :] = (10*j + i) + t * 0.1 + np.arange(Nxi + 1) * 0.5
            uv.append(arr)

    # Y block: elements n = (Ny+1)*Nx + j + (i-1)*Ny for i=1..Nx+1, j=1..Ny
    for i in range(1, Nx + 2):
        for j in range(1, Ny + 1):
            Nyj = int(np.ceil(d_y[j - 1]))
            arr = np.zeros((Nt + 1, Nyj + 1), dtype=float)
            for t in range(Nt + 1):
                arr[t, :] = (20*i + j) + t * 0.2 + np.arange(Nyj + 1) * 0.3
            uv.append(arr)

    # Choose time index t (0-based)
    t_idx = 3

    Vs = QS_complex2simple_voltage(d_x, d_y, uv, t_idx)

    print("=== QS_complex2simple_voltage testbench ===")
    print(f"Nx={Nx}, Ny={Ny}, Ns={Ns}, t_idx={t_idx}")
    print("Vs shape:", Vs.shape)

    # Show first few rows to verify mapping
    print("\nFirst 10 Vs rows [V_left, V_right]:")
    for k in range(min(10, Vs.shape[0])):
        print(f"{k+1:2d}: {Vs[k, 0]:8.3f}  {Vs[k, 1]:8.3f}")

    # Check boundaries between X and Y blocks
    x_block_rows = (Ny + 1) * Nxs
    print(f"\nRows in X block: {x_block_rows}, Y block starts at row {x_block_rows + 1}")
    print("Sample row at X-Y boundary:")
    print(f"Row {x_block_rows:2d}: {Vs[x_block_rows - 1, :]}")
    print(f"Row {x_block_rows+1:2d}: {Vs[x_block_rows, :]}")

if __name__ == "__main__":
    main()
