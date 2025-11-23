from line_geometic_factor import line_geometic_factor

def main():
    # Case 1: hai đoạn nối tiếp nhau
    x1, x2 = 0.0, 1.0
    y1, y2 = 1.0, 2.0
    I_line = line_geometic_factor(x1, x2, y1, y2)
    print("=== Testbench Case 1 ===")
    print(f"x1={x1}, x2={x2}, y1={y1}, y2={y2} -> I_line={I_line}")

    # Case 2: hai đoạn cách nhau
    x1, x2 = 0.0, 1.0
    y1, y2 = 2.0, 3.0
    I_line2 = line_geometic_factor(x1, x2, y1, y2)
    print("\n=== Testbench Case 2 ===")
    print(f"x1={x1}, x2={x2}, y1={y1}, y2={y2} -> I_line={I_line2}")

    # Case 3: đoạn thứ hai bắt đầu trước đoạn thứ nhất (sẽ được hoán đổi)
    x1, x2 = 2.0, 3.0
    y1, y2 = 0.0, 1.0
    I_line3 = line_geometic_factor(x1, x2, y1, y2)
    print("\n=== Testbench Case 3 ===")
    print(f"x1={x1}, x2={x2}, y1={y1}, y2={y2} -> I_line={I_line3}")

if __name__ == "__main__":
    main()
