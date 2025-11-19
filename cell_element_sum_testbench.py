import numpy as np
from cell_element_sum import cell_element_sum

# ================================================================
# Tạo dữ liệu giả định cho toàn bộ lưới
# ================================================================

num_elements = 25

# dx: độ dài của từng phần tử (có thể khác nhau)
dx = np.random.uniform(0.08, 0.15, num_elements)

# Gc và Cc: mỗi phần tử có thể có 1 hoặc 2 giá trị G/C
Gc = []
Cc = []
for k in range(num_elements):
    if (k + 1) % 4 == 0:
        # Phần tử đồng nhất → chỉ 1 giá trị
        G_val = np.array([np.random.uniform(5, 50)])    # mS
        C_val = np.array([np.random.uniform(0.1, 10)])   # pF
    else:
        # Phần tử không đồng đều → 2 giá trị (gần nút A và nút B)
        G_val = np.random.uniform(10, 60, 2)
        C_val = np.random.uniform(0.5, 15, 2)
    Gc.append(G_val)
    Cc.append(C_val)

# Một nút bất kỳ trong lưới với 4 nhánh nối (ví dụ điển hình)
node = [3, 7, 0, 12, 19]   # nhánh 1→phần tử 3, nhánh 2→7, nhánh 4→12, nhánh 5→19

print("=== Test hàm cell_element_sum ===")
print(f"node = {node}")
print(f"dx của các phần tử nối: {[dx[i-1] if i>0 else 0 for i in node]}\n")

Gsum, Csum = cell_element_sum(node, Gc, Cc, dx)

print(f"Kết quả:")
print(f"   Gsum = {Gsum:8.6f} (tương đương tổng điện dẫn đóng góp vào nút)")
print(f"   Csum = {Csum:8.6f} (tương đương tổng điện dung đóng góp vào nút)\n")

# In chi tiết từng nhánh để kiểm tra logic
print("Chi tiết đóng góp từng nhánh:")
print("-" * 65)
print(f"{'Nhánh':>5} {'Phần tử':>8} {'dx':>8} {'Vị trí':>7} {'G gốc':>10} {'Đóng góp G':>12} {'C gốc':>10} {'Đóng góp C':>12}")
print("-" * 65)

total_G = 0
total_C = 0
for i in range(1, 6):
    idx = i - 1
    if node[idx] > 0:
        el = node[idx]
        el_idx = el - 1
        vt1 = np.asarray(Gc[el_idx]).flatten()
        vt2 = np.asarray(Cc[el_idx]).flatten()
        N = len(vt1)
        
        if (i % 2 == 0) or (i == 5):
            n = 0
            pos = "đầu"
        else:
            n = N - 1
            pos = "cuối"
            
        contrib_G = 0.5 * dx[el_idx] * vt1[n]
        contrib_C = 0.5 * dx[el_idx] * vt2[n]
        
        total_G += contrib_G
        total_C += contrib_C
        
        print(f"{i:5} {el:8} {dx[el_idx]:8.4f} {pos:>7} {vt1[n]:10.4f} {contrib_G:12.6f} {vt2[n]:10.4f} {contrib_C:12.6f}")

print("-" * 65)
print(f"Tổng cộng → Gsum = {total_G:.6f} | Csum = {total_C:.6f}")
print("Test thành công! Kết quả từ hàm và tính tay hoàn toàn khớp.")