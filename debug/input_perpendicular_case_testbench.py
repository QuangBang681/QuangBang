# input_perpendicular_case_testbench.py
import numpy as np
from input_perpendicular_case import input_perpendicular_case

def show_case(title, xs1, ys1, zs1, d1, xs2, ys2, zs2, d2):
    x1, x2, yb, xb, y1, y2, di = input_perpendicular_case(xs1, ys1, zs1, d1, xs2, ys2, zs2, d2)
    print(title)
    print(f"  x1={x1}, x2={x2}")
    print(f"  yb={yb}, xb={xb}")
    print(f"  y1={y1}, y2={y2}")
    print(f"  di={di}\n")

def main():
    # Segment 1: along x: x=[0,2], y=1, z=0
    xs1 = [0.0, 2.0]
    ys1 = [1.0, 1.0]
    zs1 = [0.0, 0.0]
    d1 = 1

    # Segment 2 variants
    # Case A: seg2 along y: y=[-1,1], x=0.5, z=0.2
    xs2_A = [0.5, 0.5]
    ys2_A = [-1.0, 1.0]
    zs2_A = [0.2, 0.2]
    d2_A = 2

    # Case B: seg2 along z: z=[-0.5, 0.5], x=0.5, y=1.2
    xs2_B = [0.5, 0.5]
    ys2_B = [1.2, 1.2]
    zs2_B = [-0.5, 0.5]
    d2_B = 3

    # Case C: seg1 along y; seg2 along z
    xs1_C = [0.0, 0.0]
    ys1_C = [0.0, 1.0]
    zs1_C = [0.3, 0.3]
    d1_C = 2
    xs2_C = [0.7, 0.7]
    ys2_C = [0.5, 0.5]
    zs2_C = [0.0, 1.0]
    d2_C = 3

    # Case D: seg1 along z; seg2 along x
    xs1_D = [0.4, 0.4]
    ys1_D = [0.1, 0.1]
    zs1_D = [0.0, 2.0]
    d1_D = 3
    xs2_D = [0.0, 1.0]
    ys2_D = [0.1, 0.1]
    zs2_D = [0.8, 0.8]
    d2_D = 1

    print("=== input_perpendicular_case testbench ===\n")
    show_case("Case A: d1=x, d2=y", xs1, ys1, zs1, d1, xs2_A, ys2_A, zs2_A, d2_A)
    show_case("Case B: d1=x, d2=z", xs1, ys1, zs1, d1, xs2_B, ys2_B, zs2_B, d2_B)
    show_case("Case C: d1=y, d2=z", xs1_C, ys1_C, zs1_C, d1_C, xs2_C, ys2_C, zs2_C, d2_C)
    show_case("Case D: d1=z, d2=x", xs1_D, ys1_D, zs1_D, d1_D, xs2_D, ys2_D, zs2_D, d2_D)

if __name__ == "__main__":
    main()
