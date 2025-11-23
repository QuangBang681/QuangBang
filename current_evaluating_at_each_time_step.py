import numpy as np

def current_evaluating_at_each_time_step(iv, uv, Rc, Lc, t, dx, dt):
    """
    Update currents iv at time step t based on voltages uv, resistances Rc, inductances Lc.

    Parameters
    ----------
    iv : list of np.ndarray
        Each element is a 2D array (time x segments) of currents.
    uv : list of np.ndarray
        Each element is a 2D array (time x nodes) of voltages.
    Rc : list of floats or np.ndarray
        Resistance per element.
    Lc : list of floats or np.ndarray
        Inductance per element.
    t : int
        Current time index (row).
    dx : list or np.ndarray
        Lengths of each element.
    dt : float
        Time step.

    Returns
    -------
    iv : list of np.ndarray
        Updated currents with row t modified.
    """

    N = len(iv)
    k = np.zeros(N)

    for i in range(N):
        c = 2.6860  # constant for sim20
        # c = 4.5480  # alternative constant for sim100
        k[i] = (c + np.sqrt(c**2 + 4*(dx[i]/2)**2)) / (4*(dx[i]/2)*np.sqrt((dx[i]/2)**2 + c**2))

        ct = 0.005
        kt = dt / ((np.sqrt(dt**2 + ct**2) - ct) * np.sqrt(dt**2/4 + ct**2) * 2)

        Ne = iv[i].shape[1]  # number of segments
        # voltage difference between adjacent nodes at t-1
        delta_uv = uv[i][t-1, 0:Ne] - uv[i][t-1, 1:Ne+1]

        iv[i][t, :] = (1.0 / (Lc[i]*kt + Rc[i]/2)) * (
            delta_uv * k[i] + (Lc[i]*kt - Rc[i]/2) * iv[i][t-1, :]
        )

    return iv
