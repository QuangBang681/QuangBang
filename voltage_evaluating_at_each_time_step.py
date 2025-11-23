# voltage_evaluating_at_each_time_step.py
import numpy as np

def voltage_evaluating_at_each_time_step(iv, uv, V, element, Gc, Cc, t, dx, dt):
    """
    Update segment endpoint voltages at time step t using RBF-MQ scheme.

    Parameters
    ----------
    iv : list of np.ndarray
        iv[i] has shape (Nt+1, Ne_i), currents per segment for element i.
    uv : list of np.ndarray
        uv[i] has shape (Nt+1, Ne_i+1), endpoint voltages for element i.
    V : np.ndarray
        Node voltages vector (length Nnodes).
    element : np.ndarray
        Element-to-node mapping, shape (N, 2). Assumed 1-based node indices.
        element[i,0] = left/bottom node id, element[i,1] = right/top node id or 0 for open end.
    Gc : list of np.ndarray
        Conductance per segment for each element; Gc[i] has length Ne_i.
    Cc : list of np.ndarray
        Capacitance per segment for each element; Cc[i] has length Ne_i.
    t : int
        Current time index (0-based).
    dx : np.ndarray
        Spatial step per element (length N), used to compute k(i) in RBF-MQ.
    dt : float
        Time step.

    Returns
    -------
    uv : list of np.ndarray
        Updated uv with row t set for each element.
    """
    N = len(iv)

    # RBF-MQ parameters (active block)
    c = 2.6860  # for tsim ~ 20 microseconds
    ct = 0.005
    kt = dt / ((np.sqrt(dt**2 + ct**2) - ct) * np.sqrt(dt**2 / 4 + ct**2) * 2)

    # Precompute k(i) per element from dx[i] (RBF-MQ)
    k = np.empty(N, dtype=float)
    for i in range(N):
        h = dx[i] / 2.0
        k[i] = (c + np.sqrt(c**2 + 4*h**2)) / (4*h*np.sqrt(h**2 + c**2))

    for i in range(N):
        Ne = iv[i].shape[1]  # number of segments in element i

        # Map nodes: element contains 1-based indices (MATLAB style)
        left_node = int(element[i, 0])
        right_node = int(element[i, 1])

        # Left/bottom endpoint voltage from node V
        if left_node != 0:
            uv[i][t, 0] = V[left_node - 1]
        else:
            # If a left node id is 0 (rare), keep previous or set 0
            uv[i][t, 0] = uv[i][t-1, 0] if t > 0 else 0.0

        # Right/top endpoint voltage: node or open-end update
        if right_node != 0:
            uv[i][t, Ne] = V[right_node - 1]
        else:
            # Open end boundary condition
            # uv[i](t, Ne+1) in MATLAB corresponds to uv[i][t, Ne] in Python
            # Uses last segment's Cc and Gc values (index Ne-1)
            Ce = Cc[i][Ne - 1]
            Ge = Gc[i][Ne - 1]
            prev_uv_end = uv[i][t - 1, Ne] if t > 0 else 0.0
            uv[i][t, Ne] = 1.0 / (Ce / 2.0 * kt + Ge / 4.0) * (
                iv[i][t, Ne - 1] * k[i] + (Ce / 2.0 * kt - Ge / 4.0) * prev_uv_end
            )

        # Interior endpoints (columns 1..Ne-1): average segment parameters
        if Ne >= 2:
            G = 0.5 * (Gc[i][0:Ne - 1] + Gc[i][1:Ne])
            C = 0.5 * (Cc[i][0:Ne - 1] + Cc[i][1:Ne])

            prev_uv_interior = uv[i][t - 1, 1:Ne] if t > 0 else np.zeros(Ne - 1)
            delta_i = iv[i][t, 0:Ne - 1] - iv[i][t, 1:Ne]

            uv[i][t, 1:Ne] = 1.0 / (C * kt + G / 2.0) * (
                delta_i * k[i] + (C * kt - G / 2.0) * prev_uv_interior
            )

    return uv
