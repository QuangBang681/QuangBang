def locating_node_position(n, Nx):

    i = n % (Nx + 1)
    j = n // (Nx + 1) + 1

    if i == 0:
        i = Nx + 1
        j = j - 1

    return i, j
