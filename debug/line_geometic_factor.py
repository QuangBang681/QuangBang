import numpy as np

def line_geometic_factor(x1, x2, y1, y2):
    """
    Compute line geometric factor between two collinear segments.

    Parameters
    ----------
    x1, x2 : float
        Start and end coordinates of the first segment.
    y1, y2 : float
        Start and end coordinates of the second segment.

    Returns
    -------
    I_line : float
        Geometric factor value.
    """

    # Ensure the first segment starts before the second
    if y1 < x1:
        xt1, xt2 = x1, x2
        x1, x2 = y1, y2
        y1, y2 = xt1, xt2

    if np.isclose(x2, y1):  # two segments are adjacent
        I_line = (y1 * np.log(abs((y2 - x2) / (y1 - x1)))
                  - x1 * np.log(abs((y2 - x1) / (y1 - x1)))
                  + y2 * np.log(abs((y2 - x1) / (y2 - x2))))
    else:  # general case
        I_line = (x2 * np.log(abs((y2 - x2) / (y1 - x2)))
                  - x1 * np.log(abs((y2 - x1) / (y1 - x1)))
                  + y2 * np.log(abs((y2 - x1) / (y2 - x2)))
                  - y1 * np.log(abs((y1 - x1) / (y1 - x2))))
    return I_line
