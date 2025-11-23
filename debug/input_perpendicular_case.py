# input_perpendicular_case.py
import numpy as np

def input_perpendicular_case(xs1, ys1, zs1, d1, xs2, ys2, zs2, d2):
    """
    Map coordinates for two perpendicular segments based on their axes.

    Parameters
    ----------
    xs1, ys1, zs1 : array-like of length 2
        Segment 1 coordinates along x, y, z respectively.
    d1 : int
        Axis of segment 1: 1->x, 2->y, 3->z.
    xs2, ys2, zs2 : array-like of length 2
        Segment 2 coordinates along x, y, z respectively.
    d2 : int
        Axis of segment 2: 1->x, 2->y, 3->z.

    Returns
    -------
    x1, x2 : float
        The endpoints of the segment aligned with x for the computation.
    yb, xb : float
        Base coordinates (intersection coordinates) along the orthogonal axes.
        yb: base coordinate from segment 1 along the orthogonal axis.
        xb: base coordinate from segment 2 along the orthogonal axis.
    y1, y2 : float
        The endpoints of the segment aligned with the orthogonal axis.
    di : float
        Absolute separation along the remaining perpendicular axis.
    """
    xs1 = np.asarray(xs1)
    ys1 = np.asarray(ys1)
    zs1 = np.asarray(zs1)
    xs2 = np.asarray(xs2)
    ys2 = np.asarray(ys2)
    zs2 = np.asarray(zs2)

    if d1 == 1:  # x ---> x
        if d2 == 2:  # y ---> y
            x1, x2 = xs1[0], xs1[1]
            yb = ys1[0]
            xb = xs2[0]
            y1, y2 = ys2[0], ys2[1]
            di = abs(zs1[0] - zs2[0])
        else:  # y ---> z (i.e., d2 == 3)
            x1, x2 = xs1[0], xs1[1]
            yb = zs1[0]
            xb = xs2[0]
            y1, y2 = zs2[0], zs2[1]
            di = abs(ys1[0] - ys2[0])

    elif d1 == 2:  # x ---> y
        if d2 == 3:  # y ---> z
            x1, x2 = ys1[0], ys1[1]
            yb = zs1[0]
            xb = ys2[0]
            y1, y2 = zs2[0], zs2[1]
            di = abs(xs1[0] - xs2[0])
        else:  # y ---> x (i.e., d2 == 1)
            x1, x2 = ys1[0], ys1[1]
            yb = xs1[0]
            xb = ys2[0]
            y1, y2 = xs2[0], xs2[1]
            di = abs(zs1[0] - zs2[0])

    else:  # d1 == 3, x ---> z
        if d2 == 1:  # y ---> x
            x1, x2 = zs1[0], zs1[1]
            yb = xs1[0]
            xb = zs2[0]
            y1, y2 = xs2[0], xs2[1]
            di = abs(ys1[0] - ys2[0])
        else:  # y ---> y (i.e., d2 == 2)
            x1, x2 = zs1[0], zs1[1]
            yb = ys1[0]
            xb = zs2[0]
            y1, y2 = ys2[0], ys2[1]
            di = abs(xs1[0] - xs2[0])

    return x1, x2, yb, xb, y1, y2, di
