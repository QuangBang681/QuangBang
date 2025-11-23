import numpy as np
from generally_coupling_coefficients_evaluating import generally_coupling_coefficients_evaluating

def main():
    # Ví dụ nhỏ: N=3
    iv = [1.0, 2.0, 3.0]       # currents
    u_ave = [0.5, 1.0, 1.5]    # voltages
    g = [0.1, 0.2, 0.3]        # conductances
    ca = [1.0, 2.0, 3.0]       # capacitances

    Aj_i, Bj_i, Dj_i = generally_coupling_coefficients_evaluating(iv, u_ave, g, ca)

    print("=== Testbench Result ===")
    print("Aj_i:\n", Aj_i)
    print("\nBj_i:\n", Bj_i)
    print("\nDj_i:\n", Dj_i)

if __name__ == "__main__":
    main()
