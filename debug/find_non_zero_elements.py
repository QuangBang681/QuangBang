# find_non_zero_elements.py

def find_non_zero_elements(M):
    """
    Trả về danh sách chỉ số (1-based, giống MATLAB) của các phần tử khác 0 trong M.
    Nếu không có phần tử khác 0, trả về danh sách rỗng [].
    """
    non_zero = []
    for i, v in enumerate(M, start=1):  # start=1 để chỉ số giống MATLAB
        if v != 0:
            non_zero.append(i)
    return non_zero
