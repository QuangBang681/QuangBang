import numpy as np

def per_unit_length_parameter_evaluating_at_each_time_step(Aj_i, Bj_i, Dj_i, R, P, L):


    # Conductance
    F = R @ Aj_i
    Gs = 1.0 / np.diag(F)

    # Capacitance
    F = P @ Bj_i
    Cs = 1.0 / np.diag(F)

    # Inductance
    F = L @ Dj_i
    Ls = np.diag(F)

    # Convert to row vectors
    Gs = Gs.reshape(1, -1)
    Cs = Cs.reshape(1, -1)
    Ls = Ls.reshape(1, -1)

    return Gs, Cs, Ls
