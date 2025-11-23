import numpy as np
from scipy.integrate import dblquad

def parallel_geometic_factor(d, x1, x2, y1, y2):
    """
    Compute parallel geometric factor between two parallel line segments.

    Parameters
    ----------
    d : float
        Vertical distance between the two parallel segments.
    x1, x2 : float
        Start and end coordinates of the upper segment (along x-axis).
    y1, y2 : float
        Start and end coordinates of the lower segment (along y-axis).

    Returns
    -------
    I_par : float
        Value of the double integral representing the geometric factor.
    """

    # integrand: 1/sqrt((x-y)^2 + d^2)
    def f(y, x):  # note: dblquad expects f(y,x)
        return 1.0 / np.sqrt((x - y)**2 + d**2)

    I_par, _ = dblquad(f, x1, x2, lambda x: y1, lambda x: y2)
    return I_par
