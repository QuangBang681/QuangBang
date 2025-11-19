from comparing import comparing

def run_tests():
    test_cases = [
        (2, 5),    # x>0, y>x => 2/5 = 0.4
        (7, 3),    # y>0, x>=y => 1
        (0, 10),   # x=0 => else => 0
        (3, 0),    # y=0 => else => 0
        (-4, 8),   # x<0 => else => 0
        (6, 6),    # y>0, x>=y => 1
        (0, 0),    # cả hai bằng 0 => 0
    ]

    for i, (x, y) in enumerate(test_cases, 1):
        result = comparing(x, y)
        print(f"Test {i}: comparing({x}, {y}) = {result}")

if __name__ == "__main__":
    run_tests()
