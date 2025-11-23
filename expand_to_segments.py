import numpy as np

def expand_to_segments(d_x, d_y, p_z, values):
    """
    Expand per-element values (values) into per-segment vector Xs.

    Parameters
    ----------
    d_x : array-like
        Lengths of grid cells along x direction.
    d_y : array-like
        Lengths of grid cells along y direction.
    p_z : array-like
        Rod lengths at grid nodes (zero means no rod).
    values : array-like
        Per-element values (length = number of elements).

    Returns
    -------
    Xs : np.ndarray
        Expanded vector of length Ns (number of segments).
    """
    d_x = np.asarray(d_x, dtype=float)
    d_y = np.asarray(d_y, dtype=float)
    p_z = np.asarray(p_z, dtype=float)
    values = np.asarray(values, dtype=float)

    Nx = len(d_x)
    Ny = len(d_y)

    Xs_segments = []
    idx = 0

    # X-direction elements
    for j in range(Ny+1):
        for i in range(Nx):
            Nxi = int(np.ceil(d_x[i]))
            Xs_segments.extend([values[idx]]*Nxi)
            idx += 1

    # Y-direction elements
    for i in range(Nx+1):
        for j in range(Ny):
            Nyj = int(np.ceil(d_y[j]))
            Xs_segments.extend([values[idx]]*Nyj)
            idx += 1

    # Z rods
    for k, lk in enumerate(p_z):
        if lk > 0:
            Nzk = int(np.ceil(lk))
            Xs_segments.extend([values[idx]]*Nzk)
            idx += 1

    return np.array(Xs_segments)
