from element_order_locating import element_order_locating

def main():
    rod = [5, 8, 10, 12]

    # Case 1: a is present
    a = 8
    ith = element_order_locating(a, rod)
    print(f"Case 1: a={a}, rod={rod} -> ith={ith}")

    # Case 2: a is present at last position
    a = 12
    ith = element_order_locating(a, rod)
    print(f"Case 2: a={a}, rod={rod} -> ith={ith}")

    # Case 3: a is not present
    a = 7
    ith = element_order_locating(a, rod)
    print(f"Case 3: a={a}, rod={rod} -> ith={ith} (default to len(rod))")

    # Case 4: rod is empty
    rod_empty = []
    a = 1
    ith = element_order_locating(a, rod_empty)
    print(f"Case 4: a={a}, rod={rod_empty} -> ith={ith}")

if __name__ == "__main__":
    main()
