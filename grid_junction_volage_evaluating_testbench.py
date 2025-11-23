import numpy as np
from grid_junction_volage_evaluating import grid_junction_volage_evaluating

def main():
    # Số phần tử = 6, mỗi phần tử có 1 hoặc 2 nhánh dòng, thời gian là trục đầu tiên
    total_timesteps = 100
    num_elements = 6

    # ĐÚNG: iv[element, branch, time] → nhưng ta sẽ làm iv[element][time, branch]
    # Cách chuẩn nhất trong Python: iv.shape = (num_elements, total_timesteps, num_branches)
    iv = np.zeros((num_elements, total_timesteps, 2))  # 2 nhánh (hoặc 1 cũng được)

    # Gán giá trị giả lập cho vui
    for elem in range(num_elements):
        iv[elem, :, 0] = (elem + 1) * 10 + np.linspace(0, 5, total_timesteps)  # dòng nhánh 1
        iv[elem, :, 1] = (elem + 1) * 5  + np.linspace(0, 2, total_timesteps)   # dòng nhánh 2 (nếu có)

    # Nếu bạn muốn chỉ 1 nhánh thì dùng:
    # iv = np.zeros((num_elements, total_timesteps, 1))

    V = np.zeros(3)
    node = np.array([
        [1, 2, 3, 4, 0, 0],
        [2, 3, 4, 5, 0, 0],
        [3, 4, 5, 6, 0, 0]
    ], dtype=int)

    uv = np.zeros(3)
    t = 10  # bước thời gian bất kỳ từ 0 đến 99
    Gc = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
    Cc = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
    Ims = np.array([0.0, 100000.0, 0.0])  # sét đánh mạnh vào nút 2
    dx = np.ones(6)
    dt = 1e-8  # thời gian bước nhỏ cho mô phỏng sét

    V_updated = grid_junction_volage_evaluating(V, node, iv, uv, t, Gc, Cc, Ims, dx, dt)
    print("=== Testbench Result ===")
    print("Updated voltages at t =", t, ":", V_updated)

if __name__ == "__main__":
    main()
