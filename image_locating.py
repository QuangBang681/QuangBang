import numpy as np

def image_locating(z, depth):
    """
    Compute image positions of z-coordinates reflected across a plane at given depth.

    Parameters
    ----------
    z : list or np.ndarray
        Vector of z-coordinates (length 2).
    depth : float
        Depth of reflecting plane.

    Returns
    -------
    z_image : np.ndarray
        Vector of mirrored z-coordinates (length 2).
    """
    z = np.asarray(z)
    z_image = -z - 2 * depth * np.ones(2)
    return z_image
