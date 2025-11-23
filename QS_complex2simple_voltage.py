# QS_complex2simple_voltage.py
import numpy as np

def QS_complex2simple_voltage(d_x, d_y, uv, t):
    """
    Convert per-element voltages (complex model with positions) to a simple stacked form.

    Parameters
    ----------
    d_x : list or np.ndarray, length Nx
        Cell lengths along x direction.
    d_y : list or np.ndarray, length Ny
        Cell lengths along y direction.
    uv : list of length Nel
        uv[n] is a 2D array of shape (Nt+1, Nseg+1) with nodal voltages of element n.
        Element ordering follows the MATLAB convention:
          - X elements first: n = i + (j-1)*Nx for j=1..Ny+1, i=1..Nx
          - Y elements next: n = (Ny+1)*Nx + j + (i-1)*Ny for i=1..Nx+1, j=1..Ny
          - Z elements (if any) are ignored here by design (simple model excludes rods).
    t : int
        Time index (0-based in Python, corresponds to MATLAB t if you pass t-1).

    Returns
    -------
    Vs : np.ndarray, shape (Ns, 2)
        Stacked edge voltages for all segments (simple model).
        Column 0: left/bottom node voltage of each segment at time t.
        Column 1: right/top node voltage of each segment at time t.
    """
    d_x = np.asarray(d_x, dtype=float)
    d_y = np.asarray(d_y, dtype=float)

    Nx = len(d_x)
    Ny = len(d_y)

    Nxs = int(np.sum(np.ceil(d_x)))
    Nys = int(np.sum(np.ceil(d_y)))
    Ns = (Ny + 1) * Nxs + (Nx + 1) * Nys

    Vs = np.zeros((Ns, 2), dtype=float)

    # Sanity check (mirroring MATLAB's intent)
    if Ns != Vs.shape[0]:
        raise ValueError("Grid size does not match the number of segments in Vs.")

    # X-direction: j = 1..Ny+1, i = 1..Nx
    for j in range(1, Ny + 2):
        Nxi = 0
        Nxr = 0
        for i in range(1, Nx + 1):
            Nxr += Nxi
            Nxi = int(np.ceil(d_x[i - 1]))
            nc = i + (j - 1) * Nx              # 1-based element id in MATLAB
            idx_elem = nc - 1                  # convert to 0-based

            ns = (j - 1) * Nxs + Nxr           # 0-based segment start
            # uv[nc] shape: (Nt+1, Nxi+1)
            left = uv[idx_elem][t, 0:Nxi]      # left/bottom nodes at time t
            right = uv[idx_elem][t, 1:Nxi+1]   # right/top nodes at time t
            Vs[ns:ns + Nxi, 0] = left
            Vs[ns:ns + Nxi, 1] = right

    # Y-direction: i = 1..Nx+1, j = 1..Ny
    n0 = (Ny + 1) * Nxs
    for i in range(1, Nx + 2):
        Nyj = 0
        Nyr = 0
        for j in range(1, Ny + 1):
            Nyr += Nyj
            Nyj = int(np.ceil(d_y[j - 1]))
            nc = (Ny + 1) * Nx + j + (i - 1) * Ny
            idx_elem = nc - 1

            ns = (i - 1) * Nys + Nyr + n0
            left = uv[idx_elem][t, 0:Nyj]
            right = uv[idx_elem][t, 1:Nyj + 1]
            Vs[ns:ns + Nyj, 0] = left
            Vs[ns:ns + Nyj, 1] = right

    return Vs
