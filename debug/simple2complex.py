import numpy as np
from find_non_zero_elements import find_non_zero_elements

def simple2complex(d_x, d_y, p_z, Xs):
    """
    Map simple-model segment data Xs into complex-model per-element cells Xc.
    """
    d_x = np.asarray(d_x, dtype=float)
    d_y = np.asarray(d_y, dtype=float)
    p_z = np.asarray(p_z, dtype=float)
    Xs = np.asarray(Xs, dtype=float)

    Nx = len(d_x)
    Ny = len(d_y)

    rod = find_non_zero_elements(p_z)
    Nz = len(rod) if (len(rod) > 0 and rod[0] != 0) else 0

    Nxs = int(np.sum(np.ceil(d_x)))
    Nys = int(np.sum(np.ceil(d_y)))
    Nzs = int(np.sum(np.ceil(p_z)))
    Ns = (Ny + 1) * Nxs + (Nx + 1) * Nys + Nzs

    Nc = 2 * Nx * Ny + Nx + Ny + Nz

    # Debug in ra thông tin
    print(f"[DEBUG] Ns={Ns}, len(Xs)={len(Xs)}, Nc={Nc}")

    if Ns != len(Xs):
        raise ValueError(f"Grid size does not match number of segments in Xs. Ns={Ns}, len(Xs)={len(Xs)}")

    Xc = [None] * Nc

    # X-direction
    for j in range(1, Ny + 2):
        Nxi_prev = 0
        Nxr = 0
        for i in range(1, Nx + 1):
            Nxr += Nxi_prev
            Nxi = int(np.ceil(d_x[i - 1]))
            nc = i + (j - 1) * Nx
            idx_elem = nc - 1
            ns = (j - 1) * Nxs + Nxr
            Xc[idx_elem] = Xs[ns:ns + Nxi]
            Nxi_prev = Nxi

    # Y-direction
    base_y = (Ny + 1) * Nx
    n0 = (Ny + 1) * Nxs
    for i in range(1, Nx + 2):
        Nyj_prev = 0
        Nyr = 0
        for j in range(1, Ny + 1):
            Nyr += Nyj_prev
            Nyj = int(np.ceil(d_y[j - 1]))
            nc = base_y + j + (i - 1) * Ny
            idx_elem = nc - 1
            ns = (i - 1) * Nys + Nyr + n0
            Xc[idx_elem] = Xs[ns:ns + Nyj]
            Nyj_prev = Nyj

    # Z rods
    if Nz != 0:
        base_z = 2 * Nx * Ny + Nx + Ny
        n0 = (Ny + 1) * Nxs + (Nx + 1) * Nys
        Nzr = 0
        Nzk_prev = 0
        for k in range(1, Nz + 1):
            Nk_node_1b = int(rod[k - 1])
            lk = p_z[Nk_node_1b - 1]
            Nzr += Nzk_prev
            Nzk = int(np.ceil(lk))
            nc = base_z + k
            idx_elem = nc - 1
            ns = Nzr + n0
            Xc[idx_elem] = Xs[ns:ns + Nzk]
            Nzk_prev = Nzk

    return Xc
