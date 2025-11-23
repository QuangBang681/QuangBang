import numpy as np
from pul_parameter_matrixes import pul_parameter_matrixes

def main():
    # Example: 3 segments, one along x, one along y, one along z
    x = np.array([[0.0, 1.0],
                  [0.5, 0.5],
                  [0.0, 0.0]])
    y = np.array([[0.0, 0.0],
                  [0.0, 1.0],
                  [0.0, 0.0]])
    z = np.array([[0.0, 0.0],
                  [0.0, 0.0],
                  [0.0, 1.0]])
    r = np.array([0.01, 0.01, 0.01])
    d = np.array([1, 2, 3])  # directions: x, y, z
    depth = 1.0
    res = 100.0
    eps = 10.0

    R, P, L = pul_parameter_matrixes(x,y,z,r,d,depth,res,eps)

    print("=== pul_parameter_matrixes testbench ===")
    print("R matrix:\n", R)
    print("P matrix:\n", P)
    print("L matrix:\n", L)

if __name__ == "__main__":
    main()
