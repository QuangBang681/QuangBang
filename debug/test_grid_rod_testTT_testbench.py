import matplotlib.pyplot as plt
from test_grid_rod_testTT import test_grid_rod_testTT

def main():
    print("=== Testbench: Simulate grounding grid full ===")
    tv, uv = test_grid_rod_testTT()

    # Vẽ điện áp cột đầu tiên của phần tử đầu tiên theo thời gian (tương tự uv{1}(:,1) trong MATLAB)
    plt.figure(figsize=(8,5))
    plt.plot(tv * 1e6, uv[0][:, 0], linewidth=2)
    plt.xlabel("t (µs)")
    plt.ylabel("U (V)")
    plt.grid(True)
    plt.title("Voltage at first element, left endpoint")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
