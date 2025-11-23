import numpy as np
from comparing import comparing
from comparing_L import comparing_L

def generally_coupling_coefficients_evaluating(iv, u_ave, g, ca):
    """
    Evaluate coupling coefficient matrices Aj_i, Bj_i, Dj_i.

    Parameters
    ----------
    iv : list or np.ndarray
        Current vector at previous time step (length N).
    u_ave : list or np.ndarray
        Voltage vector at previous time step (length N).
    g : list or np.ndarray
        Earth conductance vector (length N).
    ca : list or np.ndarray
        Capacitance vector (length N).

    Returns
    -------
    Aj_i : np.ndarray
        N x N matrix of conductance-based coupling coefficients.
    Bj_i : np.ndarray
        N x N matrix of capacitance-based coupling coefficients.
    Dj_i : np.ndarray
        N x N matrix of inductance/current-based coupling coefficients.
    """

    iv = np.array(iv)
    u_ave = np.array(u_ave)
    g = np.array(g)
    ca = np.array(ca)

    N = len(iv)
    Aj_i = np.zeros((N, N))
    Bj_i = np.zeros((N, N))
    Dj_i = np.zeros((N, N))

    for j in range(N):
        v_ave_j = u_ave[j]
        i_dis_j = g[j] * v_ave_j
        q_j = ca[j] * v_ave_j

        for i in range(N):
            if i == j:
                Aj_i[j, i] = 1.0
                Bj_i[j, i] = 1.0
                Dj_i[j, i] = 1.0
            else:
                v_ave_i = u_ave[i]
                i_dis_i = g[i] * v_ave_i
                q_i = ca[i] * v_ave_i

                Aj_i[j, i] = comparing(i_dis_j, i_dis_i)
                Bj_i[j, i] = comparing(q_j, q_i)
                Dj_i[j, i] = comparing_L(iv[j], iv[i])

    return Aj_i, Bj_i, Dj_i
