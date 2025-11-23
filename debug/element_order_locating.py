def element_order_locating(a, rod):
    """
    Locate the order (index) of element 'a' inside list 'rod'.

    Parameters
    ----------
    a : int or float
        Target value to locate.
    rod : list
        List of values to search.

    Returns
    -------
    ith : int
        Index (1-based, like MATLAB) of 'a' in rod.
        If not found, returns len(rod).
    """
    N = len(rod)
    ith = N  # default if not found
    for i in range(N):
        if a == rod[i]:
            ith = i + 1  # convert to 1-based index
            break
    return ith
