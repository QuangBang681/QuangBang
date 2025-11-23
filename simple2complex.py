import numpy as np
from find_non_zero_elements import find_non_zero_elements

def simple2complex(d_x, d_y, p_z, Xs):
    """
    Map simple-model segment data Xs into complex-model per-element cells Xc.

    Parameters
    ----------
    d_x : array-like
        Lengths of grid cells along x direction.
    d_y : array-like
        Lengths of grid cells along y direction.
    p_z : array-like
        Rod lengths at grid nodes (zero means no rod).
    Xs : array-like
        Simple stacked data for all segments (X and Y bars, then Z rods).

    Returns
    -------
    Xc : list of np.ndarray
        Complex-model cell list:
        - First (Ny+1)*Nx entries: X-direction elements
        - Next (Nx+1)*Ny entries: Y-direction elements
        - Last Nz entries: Z-direction rod elements
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
    Ns = (Ny+1)*Nxs + (Nx+1)*Nys + Nzs

    Nc = 2*Nx*Ny + Nx + Ny + Nz

    # if Ns != len(Xs):
    #     raise ValueError(f"Grid size does not match number of segments in Xs. Ns={Ns}, len(Xs)={len(Xs)}")

    Xc = [None]*Nc

    # X-direction elements
    for j in range(1, Ny+2):
        Nxi_prev = 0
        Nxr = 0
        for i in range(1, Nx+1):
            Nxr += Nxi_prev
            Nxi = int(np.ceil(d_x[i-1]))
            nc = i + (j-1)*Nx
            ns = (j-1)*Nxs + Nxr
            Xc[nc-1] = Xs[ns:ns+Nxi]
            Nxi_prev = Nxi

    # Y-direction elements
    base_y = (Ny+1)*Nx
    n0 = (Ny+1)*Nxs
    for i in range(1, Nx+2):
        Nyj_prev = 0
        Nyr = 0
        for j in range(1, Ny+1):
            Nyr += Nyj_prev
            Nyj = int(np.ceil(d_y[j-1]))
            nc = base_y + j + (i-1)*Ny
            ns = (i-1)*Nys + Nyr + n0
            Xc[nc-1] = Xs[ns:ns+Nyj]
            Nyj_prev = Nyj

    # Z rods
    if Nz != 0:
        base_z = 2*Nx*Ny + Nx + Ny
        n0 = (Ny+1)*Nxs + (Nx+1)*Nys
        Nzr = 0
        Nzk_prev = 0
        for k in range(1, Nz+1):
            lk = p_z[int(rod[k-1])-1]  # rod indices are 1-based
            Nzr += Nzk_prev
            Nzk = int(np.ceil(lk))
            nc = base_z + k
            ns = Nzr + n0
            Xc[nc-1] = Xs[ns:ns+Nzk]
            Nzk_prev = Nzk

    return Xc
