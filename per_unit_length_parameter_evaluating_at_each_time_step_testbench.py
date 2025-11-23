import numpy as np
from per_unit_length_parameter_evaluating_at_each_time_step import per_unit_length_parameter_evaluating_at_each_time_step

def main():
    # Tạo dữ liệu giả
    # Kích thước ma trận: giả sử 3x3 để dễ kiểm thử
    Aj_i = np.array([[2.0, 0.0, 0.0],
                     [0.0, 3.0, 0.0],
                     [0.0, 0.0, 4.0]])
    Bj_i = np.array([[1.0, 0.0, 0.0],
                     [0.0, 2.0, 0.0],
                     [0.0, 0.0, 5.0]])
    Dj_i = np.array([[0.5, 0.0, 0.0],
                     [0.0, 1.0, 0.0],
                     [0.0, 0.0, 1.5]])

    R = np.eye(3)   # đơn giản: ma trận đơn vị
    P = np.eye(3)
    L = np.eye(3)

    Gs, Cs, Ls = per_unit_length_parameter_evaluating_at_each_time_step(Aj_i, Bj_i, Dj_i, R, P, L)

    print("=== Testbench Result ===")
    print("Gs =", Gs)
    print("Cs =", Cs)
    print("Ls =", Ls)

if __name__ == "__main__":
    main()
