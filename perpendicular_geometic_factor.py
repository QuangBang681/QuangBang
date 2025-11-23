import numpy as np
from scipy.integrate import dblquad

def perpendicular_geometic_factor(x1, x2, yb, xb, y1, y2, d):

    # integrand: 1/sqrt(x^2 + y^2 + d^2)
    def f(y, x):  # dblquad expects f(y,x)
        return 1.0 / np.sqrt(x**2 + y**2 + d**2)

    # integration bounds: shift coordinates by xb, yb
    I_per, _ = dblquad(f, x1 - xb, x2 - xb, lambda x: y1 - yb, lambda x: y2 - yb)
    return I_per


