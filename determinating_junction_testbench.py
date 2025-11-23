# determinating_junction_testbench.py
import numpy as np
from determinating_junction import determinating_junction

def main():
    # Grid: Nx=3, Ny=2
    d_x = [1.0, 1.0, 1.0]
    d_y = [1.0, 1.0]
    Nju = (len(d_x) + 1) * (len(d_y) + 1)

    # Put Z-rods at a few nodes (1-based IDs): 5 and last
    p_z = np.zeros(Nju, dtype=float)
    p_z[5 - 1] = 1.0
    p_z[Nju - 1] = 2.0

    node, element = determinating_junction(d_x, d_y, p_z)

    print("=== determinating_junction testbench ===")
    print(f"Nx={len(d_x)}, Ny={len(d_y)}, Nju={Nju}")
    print("node shape:", node.shape)
    print("element shape:", element.shape)

    # Show a few nodes
    print("\nFirst 8 nodes [kx1 kx2 ky1 ky2 kz]:")
    for idx in range(min(8, node.shape[0])):
        print(f"n={idx+1:2d}: {node[idx, :]}")

    # Check some element connections around an internal node (e.g., n=5)
    n_check = 5
    kx1, kx2, ky1, ky2, kz = node[n_check - 1, :]
    print(f"\nNode {n_check} connectivity:")
    print(f"  kx1={kx1} end2 -> {element[kx1-1, 1] if kx1>0 else 0}")
    print(f"  kx2={kx2} end1 -> {element[kx2-1, 0] if kx2>0 else 0}")
    print(f"  ky1={ky1} end2 -> {element[ky1-1, 1] if ky1>0 else 0}")
    print(f"  ky2={ky2} end1 -> {element[ky2-1, 0] if ky2>0 else 0}")
    print(f"  kz={kz}  end1 -> {element[kz-1, 0] if kz>0 else 0}")

    # Sanity: count how many X and Y elements got fully assigned
    x_count = (len(d_y) + 1) * len(d_x)
    y_count = (len(d_x) + 1) * len(d_y)
    print(f"\nExpected X elements: {x_count}, Y elements: {y_count}")

    # Check ends coverage (non-zero ends) in first block (X, then Y)
    x_ends = np.sum(np.any(element[:x_count, :] > 0, axis=1))
    y_ends = np.sum(np.any(element[x_count:x_count+y_count, :] > 0, axis=1))
    print(f"Assigned X elements (any end set): {x_ends}")
    print(f"Assigned Y elements (any end set): {y_ends}")

if __name__ == "__main__":
    main()
