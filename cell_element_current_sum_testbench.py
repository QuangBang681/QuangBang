import numpy as np
from cell_element_current_sum import cell_element_current_sum

# ================================================================
# Tạo dữ liệu giả định giống như trong mô phỏng lưới của bạn
# ================================================================

T = 200  # số bước thời gian

# Giả sử có tất cả 20 phần tử trong mạch
num_elements = 20

# iv là list gồm 20 ma trận, mỗi ma trận có dạng (T, 1) hoặc (T, 2)
iv = []
for k in range(num_elements):
    if k % 3 == 0:
        # Một số phần tử chỉ có 1 cột (ví dụ nguồn dòng, điện trở đơn)
        current = np.abs(np.sin(0.1 * np.arange(T) + k))[:, np.newaxis] * (k + 1) * 0.1
    else:
        # Hầu hết phần tử có 2 cột: cột 0 = dòng từ nút gốc ra, cột 1 = dòng vào nút gốc
        amp = (k + 1) * 0.05
        phase = k * 0.3
        col1 = amp * np.sin(0.05 * np.arange(T) + phase)      # ra khỏi nút
        col2 = -col1 + 0.01 * np.random.randn(T)               # vào nút (gần ngược lại)
        current = np.column_stack((col1, col2))
    iv.append(current)

# Một nút bất kỳ trong lưới
node = [3, 0, 8, 15, 0]    # nhánh 1 nối phần tử 3, nhánh 3 nối phần tử 8, nhánh 4 nối phần tử 15
ims  = 0.37                # nguồn độc lập bơm vào nút này

print("Bắt đầu test hàm cell_element_current_sum ...\n")
print(f"node = {node}")
print(f"ims  = {ims:.4f} A")
print("-" * 60)

for t in [0, 50, 99, 150, 199]:
    isum = cell_element_current_sum(node, iv, ims, t)
    print(f"t = {t:3d} → isum = {isum:+.6f} A")
    
    # In chi tiết từng nhánh để kiểm tra đúng logic
    print("   Chi tiết:")
    for i in range(1, 6):
        idx = i - 1
        if node[idx] > 0:
            el = int(node[idx])
            vt = iv[el-1]
            Nxi = vt.shape[1]
            if (i % 2 == 0) or (i == 5):
                n = 0
                sign = "-"
            else:
                n = Nxi - 1
                sign = "+"
            contrib = vt[t, n] if sign == "+" else -vt[t, n]
            print(f"     nhánh {i} (phần tử {el:2d}) → {sign} {vt[t, n]:+.6f} = {contrib:+.6f}")
    print()

print("Test hoàn tất! Nếu các giá trị isum gần 0 (ví dụ <1e-3) thì mô phỏng đang hội tụ tốt.")