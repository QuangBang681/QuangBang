import numpy as np
from cell_element_sum import cell_element_sum
from cell_element_current_sum import cell_element_current_sum

def grid_junction_volage_evaluating(V, node, iv, uv, t, Gc, Cc, Ims, dx, dt):
    """
    Update grid junction voltages at each time step.

    Parameters
    ----------
    V : np.ndarray
        Voltage vector at nodes (length N).
    node : np.ndarray
        Node-element connectivity matrix (N x ?).
    iv : np.ndarray
        Current vector at previous time step.
    uv : np.ndarray
        Voltage vector at previous time step (not used directly here).
    t : int
        Current time step index.
    Gc : np.ndarray
        Earth conductance vector for elements.
    Cc : np.ndarray
        Capacitance vector for elements.
    Ims : np.ndarray
        Lightning current vector at nodes (length N).
    dx : np.ndarray
        Element lengths.
    dt : float
        Time step size.

    Returns
    -------
    V : np.ndarray
        Updated voltage vector at nodes.
    """

    N = node.shape[0]
    for n in range(N):
        no = node[n, :]
        Gsum, Csum = cell_element_sum(no, Gc, Cc, dx)
        isum = cell_element_current_sum(no, iv, Ims[n], t)
        V[n] = 1.0 / (Gsum / 2.0 + Csum / dt) * (isum + (Csum / dt - Gsum / 2.0) * V[n])
    return V
