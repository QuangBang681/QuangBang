from locating_node_position import locating_node_position

def main():
    Nx = 3  # mỗi hàng có Nx+1 = 4 node

    # Case 1: n=1 -> (i=1, j=1)
    i, j = locating_node_position(1, Nx)
    print(f"Case 1: n=1, Nx={Nx} -> i={i}, j={j}")

    # Case 2: n=4 -> cuối hàng đầu tiên
    i, j = locating_node_position(4, Nx)
    print(f"Case 2: n=4, Nx={Nx} -> i={i}, j={j}")

    # Case 3: n=5 -> đầu hàng thứ 2
    i, j = locating_node_position(5, Nx)
    print(f"Case 3: n=5, Nx={Nx} -> i={i}, j={j}")

    # Case 4: n=8 -> cuối hàng thứ 2
    i, j = locating_node_position(8, Nx)
    print(f"Case 4: n=8, Nx={Nx} -> i={i}, j={j}")

    # Case 5: n=9 -> đầu hàng thứ 3
    i, j = locating_node_position(9, Nx)
    print(f"Case 5: n=9, Nx={Nx} -> i={i}, j={j}")

if __name__ == "__main__":
    main()
