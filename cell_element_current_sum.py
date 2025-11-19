import numpy as np

def cell_element_current_sum(node, iv, ims, t):
    node = np.asarray(node)
    isum = ims
    
    for i in range(1, 6):              # i từ 1 đến 5 giống MATLAB
        idx = i - 1                    # chuyển sang index Python 0-4
        if node[idx] > 0:
            element_idx = int(node[idx]) - 1   # giả sử phần tử trong iv bắt đầu từ 1
            vt = iv[element_idx]               # ma trận dòng của phần tử này
            Nxi = vt.shape[1]                  # số cột (1 hoặc 2)
            
            if (i % 2 == 0) or (i == 5):
                # Nhánh chẵn hoặc nhánh 5 → dòng chảy RA khỏi nút → lấy cột đầu, trừ đi
                n = 0          # Python index bắt đầu từ 0
                k = -1.0
            else:
                # Nhánh lẻ → dòng chảy VÀO nút → lấy cột cuối, cộng vào
                n = Nxi - 1
                k = 1.0
                
            isum += k * vt[t, n]
            
    return isum