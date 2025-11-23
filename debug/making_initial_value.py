# making_initial_value.py
import numpy as np
from find_non_zero_elements import find_non_zero_elements

def making_initial_value(Nt, d_x, d_y, p_z):
    """
    Initialize per-element time histories for currents (iv), voltages (uv), and cell sizes (dx).

    Parameters
    ----------
    Nt : int
        Number of time steps (the arrays will be allocated with Nt+1 rows).
    d_x : array-like of length Nx
        Lengths of grid cells along x direction.
    d_y : array-like of length Ny
        Lengths of grid cells along y direction.
    p_z : array-like of length (Nx+1)*(Ny+1)
        Rod lengths at grid nodes (zero means no rod at that node).

    Returns
    -------
    iv : list of length Nsum
        Each entry is a np.ndarray of shape (Nt+1, Nseg) for currents in that element.
    uv : list of length Nsum
        Each entry is a np.ndarray of shape (Nt+1, Nseg+1) for voltages in that element.
    dx : np.ndarray of shape (Nsum,)
        Spatial step size of each element segment.
    """
    d_x = np.asarray(d_x, dtype=float)
    d_y = np.asarray(d_y, dtype=float)
    p_z = np.asarray(p_z, dtype=float)

    Nx = len(d_x)
    Ny = len(d_y)

    rod = find_non_zero_elements(p_z)  # expected to return 1-based node indices; rod[0]==0 if none
    Nz = len(rod) if (len(rod) > 0 and rod[0] != 0) else 0

    Nsum = 2 * Nx * Ny + Nx + Ny + Nz

    # Use Python lists to match MATLAB cell arrays
    iv = [None] * Nsum
    uv = [None] * Nsum
    dx = np.ones(Nsum, dtype=float)

    # X-direction elements: indices n = i + (j-1)*Nx, for j=1..Ny+1, i=1..Nx
    for j in range(1, Ny + 2):
        for i in range(1, Nx + 1):
            n = i + (j - 1) * Nx  # 1-based
            idx = n - 1           # to 0-based
            Nxi = int(np.ceil(d_x[i - 1]))
            iv[idx] = np.zeros((Nt + 1, Nxi))
            uv[idx] = np.zeros((Nt + 1, Nxi + 1))
            dx[idx] = d_x[i - 1] / Nxi if Nxi > 0 else 0.0

    # Y-direction elements: indices n = (Ny+1)*Nx + j + (i-1)*Ny, for i=1..Nx+1, j=1..Ny
    base_y = (Ny + 1) * Nx
    for i in range(1, Nx + 2):
        for j in range(1, Ny + 1):
            n = base_y + j + (i - 1) * Ny  # 1-based
            idx = n - 1
            Nyj = int(np.ceil(d_y[j - 1]))
            iv[idx] = np.zeros((Nt + 1, Nyj))
            uv[idx] = np.zeros((Nt + 1, Nyj + 1))
            dx[idx] = d_y[j - 1] / Nyj if Nyj > 0 else 0.0

    # Z-direction rods: indices n = k + 2*Nx*Ny + Nx + Ny, for k=1..Nz
    if Nz != 0:
        base_z = 2 * Nx * Ny + Nx + Ny
        for k in range(1, Nz + 1):
            n = base_z + k  # 1-based
            idx = n - 1
            node_1b = int(rod[k - 1])  # 1-based node id of rod
            Nzk = int(np.ceil(p_z[node_1b - 1]))
            iv[idx] = np.zeros((Nt + 1, Nzk))
            uv[idx] = np.zeros((Nt + 1, Nzk + 1))
            dz = p_z[node_1b - 1] / Nzk if Nzk > 0 else 0.0
            dx[idx] = dz

    return iv, uv, dx
