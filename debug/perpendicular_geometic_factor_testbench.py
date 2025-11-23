from perpendicular_geometic_factor import perpendicular_geometic_factor

def main():
    # Case 1: đoạn ngang từ 0 đến 2 tại yb=0, đoạn dọc từ 0 đến 2 tại xb=0, khoảng cách d=1
    I_per = perpendicular_geometic_factor(x1=0.0, x2=2.0, yb=0.0, xb=0.0,
                                          y1=0.0, y2=2.0, d=1.0)
    print("=== Testbench Result Case 1 ===")
    print("I_per =", I_per)

    # Case 2: đoạn ngang từ 0 đến 1 tại yb=1, đoạn dọc từ 0 đến 1 tại xb=0.5, khoảng cách d=0.5
    I_per2 = perpendicular_geometic_factor(x1=0.0, x2=1.0, yb=1.0, xb=0.5,
                                           y1=0.0, y2=1.0, d=0.5)
    print("\n=== Testbench Result Case 2 ===")
    print("I_per =", I_per2)

if __name__ == "__main__":
    main()
