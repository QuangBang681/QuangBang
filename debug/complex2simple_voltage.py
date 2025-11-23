import numpy as np
from find_non_zero_elements import find_non_zero_elements  # giả định bạn có file này

def complex2simple_voltage(d_x, d_y, p_z, Vc, t):
    """
    Convert voltages from complex geometrical model to simple vector form.

    Parameters
    ----------
    d_x : list or np.ndarray
        Lengths of bars along x direction.
    d_y : list or np.ndarray
        Lengths of bars along y direction.
    p_z : list or np.ndarray
        Lengths of rods along z direction.
    Vc : list of np.ndarray
        Cell array (list) of node voltages for each element.
        Each element is a 2D array with time along axis 0 and node voltages along axis 1.
        Must have (segments+1) columns.
    t : int
        Time index (row index).

    Returns
    -------
    Vs : np.ndarray
        Flattened vector of segment voltages at time t.
    """

    Nx = len(d_x)
    Ny = len(d_y)
    rod = find_non_zero_elements(p_z)

    if len(rod) > 0 and rod[0] != 0:
        Nz = len(rod)
    else:
        Nz = 0

    Ns = (Ny + 1) * np.sum(np.ceil(d_x)) + (Nx + 1) * np.sum(np.ceil(d_y)) + np.sum(np.ceil(p_z))
    Ns = int(Ns)

    Nc = 2 * Nx * Ny + Nx + Ny + Nz

    Vs = np.zeros(Ns)

    if Ns == len(Vs):  # Thông số đúng
        # --- X-oriented bars ---
        Nxs = int(np.sum(np.ceil(d_x)))
        for j in range(Ny + 1):
            Nxi = 0
            Nxr = 0
            for i in range(Nx):
                Nxr += Nxi
                Nxi = int(np.ceil(d_x[i]))
                nc = i + j * Nx
                ns = j * Nxs + Nxr
                # average adjacent node voltages
                Vs[ns:ns + Nxi] = 0.5 * (Vc[nc][t, 0:Nxi] + Vc[nc][t, 1:Nxi+1])

        # --- Y-oriented bars ---
        Nys = int(np.sum(np.ceil(d_y)))
        n0 = (Ny + 1) * Nxs
        for i in range(Nx + 1):
            Nyj = 0
            Nyr = 0
            for j in range(Ny):
                Nyr += Nyj
                Nyj = int(np.ceil(d_y[j]))
                nc = (Ny + 1) * Nx + j + i * Ny
                ns = i * Nys + Nyr + n0
                Vs[ns:ns + Nyj] = 0.5 * (Vc[nc][t, 0:Nyj] + Vc[nc][t, 1:Nyj+1])

        # --- Z rods ---
        if Nz != 0:
            n0 = (Ny + 1) * Nxs + (Nx + 1) * Nys
            Nzr = 0
            Nzk = 0
            for k in range(Nz):
                # lk = p_z[rod[k]]
                lk = p_z[rod[k] - 1]
                Nzr += Nzk
                Nzk = int(np.ceil(lk))
                nc = k + 2 * Nx * Ny + Nx + Ny
                ns = Nzr + n0
                Vs[ns:ns + Nzk] = 0.5 * (Vc[nc][t, 0:Nzk] + Vc[nc][t, 1:Nzk+1])
    else:
        print('\nKích thước lưới không khớp với số phần tử của Vs')

    return Vs
