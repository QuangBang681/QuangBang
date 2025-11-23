import numpy as np

def expand_to_segments(d_x, d_y, p_z, values):
    """
    Expand per-element values into per-segment vector Xs.
    If values already has length = Ns (number of segments), return as-is.
    """
    d_x = np.asarray(d_x, dtype=float)
    d_y = np.asarray(d_y, dtype=float)
    p_z = np.asarray(p_z, dtype=float)
    values = np.atleast_1d(values).astype(float)

    Nx = len(d_x)
    Ny = len(d_y)

    # số element
    num_elements = (Ny+1)*Nx + (Nx+1)*Ny + np.count_nonzero(p_z)
    # số segment
    Ns = (Ny+1)*int(np.sum(np.ceil(d_x))) + (Nx+1)*int(np.sum(np.ceil(d_y))) + int(np.sum(np.ceil(p_z)))

    # Nếu values đã có độ dài bằng Ns (segment) thì trả về luôn
    if values.size == Ns:
        return values

    # Nếu values chỉ có 1 phần tử, nhân ra cho tất cả element
    if values.size == 1:
        values = np.repeat(values[0], num_elements)

    if values.size != num_elements:
        raise ValueError(f"[expand_to_segments] values length={values.size}, expected {num_elements} or {Ns}")

    Xs_segments = []
    idx = 0

    # X-direction
    for j in range(Ny+1):
        for i in range(Nx):
            Nxi = int(np.ceil(d_x[i]))
            Xs_segments.extend([values[idx]]*Nxi)
            idx += 1

    # Y-direction
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
