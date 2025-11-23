# locating_segments_position.py
import numpy as np
from find_non_zero_elements import find_non_zero_elements
from locating_node_position import locating_node_position

def locating_segments_position(d_x, d_y, p_z, rx, ry, rz):
    """
    Compute positions and attributes of all segments along x, y, z for a rectangular grid.

    Parameters
    ----------
    d_x : array-like, shape (Nx,)
        Lengths of grid cells along x direction.
    d_y : array-like, shape (Ny,)
        Lengths of grid cells along y direction.
    p_z : array-like, shape ((Nx+1)*(Ny+1),)
        Rod lengths at each grid node. Zero means no rod at that node.
    rx : array-like, shape (Ny+1, Nx)
        Radius of bars parallel to x-axis at each row j and column i.
    ry : array-like, shape (Nx+1, Ny)
        Radius of bars parallel to y-axis at each column i and row j.
    rz : array-like, shape ((Nx+1)*(Ny+1),)
        Radius of rod parallel to z-axis at each node.

    Returns
    -------
    x : np.ndarray, shape (Ns, 2)
        Segment endpoints along x for each segment n (n: 1..Ns).
    y : np.ndarray, shape (Ns, 2)
        Segment endpoints along y for each segment n.
    z : np.ndarray, shape (Ns, 2)
        Segment endpoints along z for each segment n.
    r : np.ndarray, shape (Ns,)
        Radius assigned to each segment n.
    d : np.ndarray, shape (Ns,)
        Axis code for segment n: 1 -> x, 2 -> y, 3 -> z.
    """
    d_x = np.asarray(d_x, dtype=float)
    d_y = np.asarray(d_y, dtype=float)
    p_z = np.asarray(p_z, dtype=float)
    rx = np.asarray(rx, dtype=float)
    ry = np.asarray(ry, dtype=float)
    rz = np.asarray(rz, dtype=float)

    Nx = len(d_x)
    Ny = len(d_y)

    rod = find_non_zero_elements(p_z)  # expected 1-based indices, with special rod[0]==0 if none

    Ns = int((Ny + 1) * np.sum(np.ceil(d_x)) +
             (Nx + 1) * np.sum(np.ceil(d_y)) +
             np.sum(np.ceil(p_z)))

    x = np.zeros((Ns, 2), dtype=float)
    y = np.zeros((Ns, 2), dtype=float)
    z = np.zeros((Ns, 2), dtype=float)
    d = np.ones(Ns, dtype=int)  # default axis code = 1 (x)
    r = np.copy(d).astype(float)

    # SEGMENTS ON X DIRECTION (begin at n = 1)
    z1 = 0.0
    y1 = 0.0
    Nxs = int(np.sum(np.ceil(d_x)))  # number of x-direction segments per row

    for j in range(1, Ny + 2):  # j = 1..Ny+1
        if j >= 2:
            y1 += d_y[j - 2]
        x1 = 0.0
        Nxi = 0
        Nxr = 0
        for i in range(1, Nx + 1):  # i = 1..Nx
            if i >= 2:
                x1 += d_x[i - 2]
            Nxr += Nxi
            Nxi = int(np.ceil(d_x[i - 1]))
            dx = d_x[i - 1] / Nxi if Nxi > 0 else 0.0
            for k in range(1, Nxi + 1):
                n = k + Nxr + (j - 1) * Nxs  # 1-based
                idx = n - 1                  # to 0-based
                d[idx] = 1
                r[idx] = rx[j - 1, i - 1]
                x[idx, 0] = x1 + (k - 1) * dx
                x[idx, 1] = x1 + k * dx
                y[idx, 0] = y1
                y[idx, 1] = y1
                z[idx, 0] = z1
                z[idx, 1] = z1

    # SEGMENTS ON Y DIRECTION (begin at n = 1 + (Ny+1)*Nxs)
    z1 = 0.0
    x1 = 0.0
    Nys = int(np.sum(np.ceil(d_y)))  # number of y-direction segments per column
    n0 = (Ny + 1) * Nxs

    for i in range(1, Nx + 2):  # i = 1..Nx+1
        if i >= 2:
            x1 += d_x[i - 2]
        y1 = 0.0
        Nyj = 0
        Nyr = 0
        for j in range(1, Ny + 1):  # j = 1..Ny
            if j >= 2:
                y1 += d_y[j - 2]
            Nyr += Nyj
            Nyj = int(np.ceil(d_y[j - 1]))
            dy = d_y[j - 1] / Nyj if Nyj > 0 else 0.0
            for k in range(1, Nyj + 1):
                n = n0 + k + Nyr + (i - 1) * Nys  # 1-based
                idx = n - 1
                d[idx] = 2
                r[idx] = ry[i - 1, j - 1]
                x[idx, 0] = x1
                x[idx, 1] = x1
                y[idx, 0] = y1 + (k - 1) * dy
                y[idx, 1] = y1 + k * dy
                z[idx, 0] = z1
                z[idx, 1] = z1

    # SEGMENTS ON Z DIRECTION
    if len(rod) > 0 and rod[0] != 0:
        n0 = (Ny + 1) * Nxs + (Nx + 1) * Nys
        Nz = len(rod)
        Nzs = int(np.sum(np.ceil(p_z)))
        Nzr = 0
        Nzk = 0
        for k in range(1, Nz + 1):
            node_idx_1b = int(rod[k - 1])     # 1-based node id
            lk = p_z[node_idx_1b - 1]
            Nzr += Nzk
            Nzk = int(np.ceil(lk))
            dz = lk / Nzk if Nzk > 0 else 0.0
            z1 = 0.0

            # locating node (i, j) for this rod node id
            i, j = locating_node_position(node_idx_1b, Nx)  # expected 1-based (i, j)

            x1 = 0.0
            y1 = 0.0
            if i >= 2:
                x1 = float(np.sum(d_x[:i - 1]))
            if j >= 2:
                y1 = float(np.sum(d_y[:j - 1]))

            for m in range(1, Nzk + 1):
                n = n0 + m + Nzr  # 1-based
                idx = n - 1
                d[idx] = 3
                r[idx] = rz[node_idx_1b - 1]
                x[idx, 0] = x1
                x[idx, 1] = x1
                y[idx, 0] = y1
                y[idx, 1] = y1
                z[idx, 0] = z1 + (m - 1) * dz
                z[idx, 1] = z1 + m * dz

    return x, y, z, r, d
