from test_grid_rod import test_grid_rod

def main():
    print("=== Testbench: Simulate grounding grid 1x1 ===")
    tv, uv = test_grid_rod()
    # In một vài giá trị để xác thực
    print("tv sample (µs):", [round(t*1e6, 3) for t in tv[:5]])
    print("uv[0] first row endpoints:", uv[0][0, :])

if __name__ == "__main__":
    main()
