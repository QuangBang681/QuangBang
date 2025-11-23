# locating_segments_position_testbench.py
import numpy as np
from locating_segments_position import locating_segments_position

def main():
    # Small grid: Nx=2, Ny=2
    d_x = [1.0, 1.0]
    d_y = [1.0, 1.0]

    Nx = len(d_x)
    Ny = len(d_y)
    Nju = (Nx + 1) * (Ny + 1)

    # Rods: put a rod at node 5 and node 9 (1-based ids)
    p_z = np.zeros(Nju)
    p_z[5 - 1] = 1.2
    p_z[9 - 1] = 0.5

    # Radii
    rx = np.full((Ny + 1, Nx), 0.02)  # bars along x
    ry = np.full((Nx + 1, Ny), 0.02)  # bars along y
    rz = np.full(Nju, 0.01)           # rods along z

    x, y, z, r, d = locating_segments_position(d_x, d_y, p_z, rx, ry, rz)

    Ns = x.shape[0]
    print("=== locating_segments_position testbench ===")
    print(f"Nx={Nx}, Ny={Ny}, Nju={Nju}")
    print(f"Total segments Ns={Ns}")

    # Counts expected
    Nxs = int(np.sum(np.ceil(d_x)))
    Nys = int(np.sum(np.ceil(d_y)))
    expected_x_segments = (Ny + 1) * Nxs
    expected_y_segments = (Nx + 1) * Nys
    expected_z_segments = int(np.sum(np.ceil(p_z)))
    print(f"Expected X segments: {expected_x_segments}")
    print(f"Expected Y segments: {expected_y_segments}")
    print(f"Expected Z segments: {expected_z_segments}")

    # Show first 10 segments summary
    print("\nFirst 10 segments [d, r, (x1,x2), (y1,y2), (z1,z2)]:")
    for n in range(min(10, Ns)):
        print(f"n={n+1:2d}: d={d[n]}, r={r[n]:.3f}, x={tuple(x[n])}, y={tuple(y[n])}, z={tuple(z[n])}")

    # Sanity checks: axis codes and positions for a few segments
    print("\nSample checks:")
    # First row along x (should be y=y1=0)
    print(f"Segment 1 axis d={d[0]}, y={y[0]}")
    # First y-direction segment start index
    first_y_idx = (Ny + 1) * Nxs  # 1-based start of Y block
    print(f"First Y segment at n={first_y_idx+1}: d={d[first_y_idx]}, x={x[first_y_idx]}, y={y[first_y_idx]}")
    # First z-direction segment start index
    first_z_idx = (Ny + 1) * Nxs + (Nx + 1) * Nys
    print(f"First Z segment at n={first_z_idx+1}: d={d[first_z_idx]}, x={x[first_z_idx]}, y={y[first_z_idx]}, z={z[first_z_idx]}")

if __name__ == "__main__":
    main()
