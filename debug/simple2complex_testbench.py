
# simple2complex_testbench.py
import numpy as np
from simple2complex import simple2complex

def main():
    # Grid: Nx=2, Ny=2
    d_x = [1.0, 0.6]   # ceil -> [1,1] -> Nxs = 2
    d_y = [0.8, 1.2]   # ceil -> [1,2] -> Nys = 3
    Nx, Ny = len(d_x), len(d_y)
    Nju = (Nx + 1) * (Ny + 1)

    # Rods at nodes: place rods at node 5 (length 0.75 -> ceil 1) and node 9 (length 0.5 -> ceil 1)
    p_z = np.zeros(Nju)
    p_z[5 - 1] = 0.75
    p_z[9 - 1] = 0.5
    # Total segments:
    Nxs = int(np.sum(np.ceil(d_x)))    # 2
    Nys = int(np.sum(np.ceil(d_y)))    # 3
    Nzs = int(np.sum(np.ceil(p_z)))    # 2
    Ns = (Ny + 1) * Nxs + (Nx + 1) * Nys + Nzs  # (2+1)*2 + (2+1)*3 + 2 = 6 + 9 + 2 = 17

    # Build Xs of length Ns with identifiable values
    # X-block rows per j: Nxs=2 segments each row, Ny+1=3 rows => 6 values
    # Y-block rows per i: Nys=3 segments each column, Nx+1=3 columns => 9 values
    # Z-block: 2 segments
    Xs = np.zeros(Ns)
    idx = 0

    # X block (j=1..Ny+1, i-segments by d_x)
    for j in range(1, Ny + 2):
        # For this simple example, each x element has Nxi=1 segment (ceil of d_x)
        # We'll set values per row: 10*j + k
        for k in range(1, Nxs + 1):
            Xs[idx] = 10 * j + k
            idx += 1

    # Y block (i=1..Nx+1, j-segments by d_y)
    for i in range(1, Nx + 2):
        # Values per column: 20*i + k
        for k in range(1, Nys + 1):
            Xs[idx] = 20 * i + k
            idx += 1

    # Z block (two rods)
    Xs[idx] = 30.1; idx += 1
    Xs[idx] = 30.2; idx += 1

    # Map to complex
    Xc = simple2complex(d_x, d_y, p_z, Xs)

    # Print summary
    Nc = 2 * Nx * Ny + Nx + Ny + int(np.sum(p_z > 0))
    print("=== simple2complex testbench ===")
    print(f"Nx={Nx}, Ny={Ny}, Ns={Ns}, Nc={len(Xc)}")
    print("X-block (first (Ny+1)*Nx elements):")
    for j in range(1, Ny + 2):
        for i in range(1, Nx + 1):
            nc = i + (j - 1) * Nx
            idx_elem = nc - 1
            print(f"  nc={nc:2d} (x elem j={j}, i={i}): {Xc[idx_elem]}")

    print("\nY-block (next (Nx+1)*Ny elements):")
    base_y = (Ny + 1) * Nx
    for i in range(1, Nx + 2):
        for j in range(1, Ny + 1):
            nc = base_y + j + (i - 1) * Ny
            idx_elem = nc - 1
            print(f"  nc={nc:2d} (y elem i={i}, j={j}): {Xc[idx_elem]}")

    print("\nZ-block (last Nz elements):")
    base_z = 2 * Nx * Ny + Nx + Ny
    for k in range(1, int(np.sum(p_z > 0)) + 1):
        nc = base_z + k
        idx_elem = nc - 1
        print(f"  nc={nc:2d} (z rod k={k}): {Xc[idx_elem]}")

if __name__ == "__main__":
    main()
