from parallel_geometic_factor import parallel_geometic_factor

def main():
    # Ví dụ: hai đoạn song song
    d = 1.0
    x1, x2 = 0.0, 2.0   # đoạn trên từ 0 đến 2
    y1, y2 = 0.0, 2.0   # đoạn dưới từ 0 đến 2

    I_par = parallel_geometic_factor(d, x1, x2, y1, y2)

    print("=== Testbench Result ===")
    print(f"d={d}, x1={x1}, x2={x2}, y1={y1}, y2={y2}")
    print("I_par =", I_par)

    # Thử thêm một case khác
    d2 = 0.5
    I_par2 = parallel_geometic_factor(d2, 0.0, 1.0, 0.0, 1.0)
    print("\nCase 2: d=0.5, x1=0, x2=1, y1=0, y2=1")
    print("I_par =", I_par2)

if __name__ == "__main__":
    main()
