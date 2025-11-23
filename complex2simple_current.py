import numpy as np
from find_non_zero_elements import find_non_zero_elements

def complex2simple_current(d_x, d_y, p_z, Ic, t):
    """
    Convert currents from complex geometrical model to simple vector form.

    Parameters
    ----------
    d_x : list or np.ndarray
        Lengths of bars along x direction.
    d_y : list or np.ndarray
        Lengths of bars along y direction.
    p_z : list or np.ndarray
        Lengths of rods along z direction.
    Ic : list of np.ndarray
        Cell array (list) of current data for each element.
        Each element is a 2D array with time along axis 0.
    t : int
        Time index (row index).

    Returns
    -------
    Is : np.ndarray
        Flattened vector of currents at time t.
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

    Is = np.zeros(Ns)

    if Ns == len(Is):  # Thông số đúng
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
                Is[ns:ns + Nxi] = Ic[nc][t, :]
        
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
                Is[ns:ns + Nyj] = Ic[nc][t, :]
        
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
                Is[ns:ns + Nzk] = Ic[nc][t, :]
    else:
        print('\nKích thước lưới không khớp với số phần tử của Xs')

    return Is
