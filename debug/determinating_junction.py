# determinating_junction.py
import numpy as np
from find_non_zero_elements import find_non_zero_elements
from element_order_locating import element_order_locating

def determinating_junction(d_x, d_y, p_z):
    """
    Build node and element connectivity matrices for a rectangular grid with optional Z-rods.

    Parameters
    ----------
    d_x : list or np.ndarray
        Segment lengths along x direction (Nx entries).
    d_y : list or np.ndarray
        Segment lengths along y direction (Ny entries).
    p_z : list or np.ndarray
        Per-node values indicating presence of a Z-rod at node n (non-zero => has rod).
        Length must be Nju = (Nx+1)*(Ny+1). Uses MATLAB-like node indexing (1-based IDs).

    Returns
    -------
    node : np.ndarray
        Shape (Nju, 5). For each node n (1-based):
        [kx1, kx2, ky1, ky2, kz] where 0 indicates "no element" on that side.
    element : np.ndarray
        Shape (Nel, 2). For each element id k (1-based):
        [end1, end2] node IDs (1-based). 0 indicates unset (e.g., for rods' second end).
    """
    Nx = len(d_x)
    Ny = len(d_y)

    rod = find_non_zero_elements(p_z)
    Nz = len(rod) if (len(rod) > 0 and rod[0] != 0) else 0

    Nju = (Nx + 1) * (Ny + 1)
    Nel = 2 * Nx * Ny + Nx + Ny + Nz
    nxe = (Ny + 1) * Nx                 # number of X elements
    nye = 2 * Nx * Ny + Nx + Ny         # offset start of Z elements

    node = np.zeros((Nju, 5), dtype=int)
    element = np.zeros((Nel, 2), dtype=int)

    def set_element_end(k, col, n):
        # k is 1-based. Only set if k>0.
        if k > 0:
            element[k - 1, col] = n

    # Internal nodes: 2<=i<=Nx, 2<=j<=Ny
    for j in range(2, Ny + 1):
        for i in range(2, Nx + 1):
            n = i + (j - 1) * (Nx + 1)
            kx1 = i - 1 + (j - 1) * Nx
            kx2 = i + (j - 1) * Nx
            ky1 = nxe + j - 1 + (i - 1) * Ny
            ky2 = nxe + j + (i - 1) * Ny

            set_element_end(kx1, 1, n)  # end2
            set_element_end(kx2, 0, n)  # end1
            set_element_end(ky1, 1, n)  # end2
            set_element_end(ky2, 0, n)  # end1

            if p_z[n - 1] != 0:
                cz = element_order_locating(n, rod)
                kz = nye + cz
                set_element_end(kz, 0, n)
            else:
                kz = 0

            node[n - 1, :] = [kx1, kx2, ky1, ky2, kz]

    # Boundaries j=1 and j=Ny+1 (for i=2..Nx)
    for i in range(2, Nx + 1):
        # j=1
        n = i
        kx1 = i - 1
        kx2 = i
        ky1 = 0
        ky2 = nxe + 1 + (i - 1) * Ny

        set_element_end(kx1, 1, n)  # end2
        set_element_end(kx2, 0, n)  # end1
        # ky1 skipped (0)
        set_element_end(ky2, 0, n)  # end1

        if p_z[n - 1] != 0:
            cz = element_order_locating(n, rod)
            kz = nye + cz
            set_element_end(kz, 0, n)
        else:
            kz = 0
        node[n - 1, :] = [kx1, kx2, ky1, ky2, kz]

        # j=Ny+1
        n = i + Ny * (Nx + 1)
        kx1 = i - 1 + Ny * Nx
        kx2 = i + Ny * Nx
        ky1 = nxe + Ny + (i - 1) * Ny
        ky2 = 0

        set_element_end(kx1, 1, n)  # end2
        set_element_end(kx2, 0, n)  # end1
        set_element_end(ky1, 1, n)  # end2
        # ky2 skipped (0)

        if p_z[n - 1] != 0:
            cz = element_order_locating(n, rod)
            kz = nye + cz
            set_element_end(kz, 0, n)
        else:
            kz = 0
        node[n - 1, :] = [kx1, kx2, ky1, ky2, kz]

    # Boundaries i=1 and i=Nx+1 (for j=2..Ny)
    for j in range(2, Ny + 1):
        # i=1
        n = 1 + (j - 1) * (Nx + 1)
        kx1 = 0
        kx2 = 1 + (j - 1) * Nx
        ky1 = nxe + j - 1
        ky2 = nxe + j

        # kx1 skipped (0)
        set_element_end(kx2, 0, n)  # end1
        set_element_end(ky1, 1, n)  # end2
        set_element_end(ky2, 0, n)  # end1

        if p_z[n - 1] != 0:
            cz = element_order_locating(n, rod)
            kz = nye + cz
            set_element_end(kz, 0, n)
        else:
            kz = 0
        node[n - 1, :] = [kx1, kx2, ky1, ky2, kz]

        # i=Nx+1
        n = Nx + 1 + (j - 1) * (Nx + 1)
        kx1 = Nx + (j - 1) * Nx
        kx2 = 0
        ky1 = nxe + j - 1 + Nx * Ny
        ky2 = nxe + j + Nx * Ny

        set_element_end(kx1, 1, n)  # end2
        # kx2 skipped (0)
        set_element_end(ky1, 1, n)  # end2
        set_element_end(ky2, 0, n)  # end1

        if p_z[n - 1] != 0:
            cz = element_order_locating(n, rod)
            kz = nye + cz
            set_element_end(kz, 0, n)
        else:
            kz = 0
        node[n - 1, :] = [kx1, kx2, ky1, ky2, kz]

    # Corners
    # i=1, j=1
    n = 1
    kx1 = 0
    kx2 = 1
    ky1 = 0
    ky2 = nxe + 1
    # kx1 skipped
    set_element_end(kx2, 0, n)
    # ky1 skipped
    set_element_end(ky2, 0, n)
    if p_z[n - 1] != 0:
        cz = element_order_locating(n, rod)
        kz = nye + cz
        set_element_end(kz, 0, n)
    else:
        kz = 0
    node[n - 1, :] = [kx1, kx2, ky1, ky2, kz]

    # i=1, j=Ny+1
    n = 1 + Ny * (Nx + 1)
    kx1 = 0
    kx2 = 1 + Ny * Nx
    ky1 = nxe + Ny
    ky2 = 0
    # kx1 skipped
    set_element_end(kx2, 0, n)
    set_element_end(ky1, 1, n)
    # ky2 skipped
    if p_z[n - 1] != 0:
        cz = element_order_locating(n, rod)
        kz = nye + cz
        set_element_end(kz, 0, n)
    else:
        kz = 0
    node[n - 1, :] = [kx1, kx2, ky1, ky2, kz]

    # i=Nx+1, j=1
    n = Nx + 1
    kx1 = Nx
    kx2 = 0
    ky1 = 0
    ky2 = nxe + 1 + Nx * Ny
    set_element_end(kx1, 1, n)
    # kx2 skipped
    # ky1 skipped
    set_element_end(ky2, 0, n)
    if p_z[n - 1] != 0:
        cz = element_order_locating(n, rod)
        kz = nye + cz
        set_element_end(kz, 0, n)
    else:
        kz = 0
    node[n - 1, :] = [kx1, kx2, ky1, ky2, kz]

    # i=Nx+1, j=Ny+1
    n = (Ny + 1) * (Nx + 1)
    kx1 = (Ny + 1) * Nx
    kx2 = 0
    ky1 = nxe + (Nx + 1) * Ny
    ky2 = 0
    set_element_end(kx1, 1, n)
    # kx2 skipped
    set_element_end(ky1, 1, n)
    # ky2 skipped
    if p_z[n - 1] != 0:
        cz = element_order_locating(n, rod)
        kz = nye + cz
        set_element_end(kz, 0, n)
    else:
        kz = 0
    node[n - 1, :] = [kx1, kx2, ky1, ky2, kz]

    return node, element
