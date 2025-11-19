import numpy as np

def cell_element_sum(node, Gc, Cc, dx):

    node = np.asarray(node, dtype=int)
    dx = np.asarray(dx, dtype=float)
    Gsum = 0.0
    Csum = 0.0
    
    for i in range(1, 6):              # i từ 1 đến 5 như MATLAB
        idx = i - 1                    # index Python: 0-4
        if node[idx] > 0:
            el = node[idx]             # chỉ số phần tử (1-based)
            el_idx = el - 1            # chuyển sang index Python của list
            
            vt1 = np.asarray(Gc[el_idx]).flatten()  # vector G của phần tử này
            vt2 = np.asarray(Cc[el_idx]).flatten()  # vector C
            
            Nxi = len(vt1)
            
            if (i % 2 == 0) or (i == 5):
                n = 0                  # lấy đầu tiên (gần nút bên kia)
            else:
                n = Nxi - 1            # lấy cuối cùng (gần nút hiện tại)
                
            factor = 0.5 * dx[el_idx]
            Gsum += factor * vt1[n]
            Csum += factor * vt2[n]
            
    return Gsum, Csum