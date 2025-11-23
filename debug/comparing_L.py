def comparing_L(x, y):

    ax = abs(x)
    ay = abs(y)

    if ax > 0 and ay >= ax:
        return ax / ay
    elif ax > ay:
        return 1
    else:
        return 0
