# test_find_non_zero_elements.py
from find_non_zero_elements import find_non_zero_elements

def run_tests():
    test_cases = [
        [-1, 3, 0, -1, 5],   # có phần tử khác 0 ở vị trí 2,4,5
        [0, 0, 0],          # toàn bộ bằng 0
        [7, 0, 9],          # khác 0 ở vị trí 1,3
        [],                 # mảng rỗng
        [1, -2, 3, 4],      # tất cả khác 0
    ]

    for i, M in enumerate(test_cases, 1):
        result = find_non_zero_elements(M)
        print(f"Test {i}: M = {M} -> non_zero indices = {result}")

if __name__ == "__main__":
    run_tests()
