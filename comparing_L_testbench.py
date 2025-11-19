# test_comparing_L.py
from comparing_L import comparing_L

def run_tests():
    test_cases = [
        (2, 5),    # |y| >= |x| > 0 => 2/5 = 0.4
        (7, 3),    # |x| > |y| => 1
        (0, 10),   # x = 0 => 0
        (3, 0),    # |x| > |y|=0 => 1
        (-4, 8),   # |x|=4, |y|=8 => 4/8 = 0.5
        (-6, -2),  # |x|=6 > |y|=2 => 1
        (0, 0),    # cả hai bằng 0 => 0
    ]

    for i, (x, y) in enumerate(test_cases, 1):
        result = comparing_L(x, y)
        print(f"Test {i}: comparing_L({x}, {y}) = {result}")

if __name__ == "__main__":
    run_tests()
