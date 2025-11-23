import numpy as np
from image_locating import image_locating
from line_geometic_factor import line_geometic_factor
from parallel_geometic_factor import parallel_geometic_factor
from perpendicular_geometic_factor import perpendicular_geometic_factor
from input_perpendicular_case import input_perpendicular_case

def pul_parameter_matrixes(x, y, z, r, d, depth, res, eps):
    """
    Compute per-unit-length parameter matrices R, P, L for a grounding grid.

    Parameters
    ----------
    x, y, z : np.ndarray, shape (N,2)
        Segment endpoints along x, y, z.
    r : np.ndarray, shape (N,)
        Radius of each segment.
    d : np.ndarray, shape (N,)
        Axis code: 1->x, 2->y, 3->z.
    depth : float
        Ground depth for image method.
    res : float
        Soil resistivity.
    eps : float
        Soil relative permittivity.

    Returns
    -------
    R, P, L : np.ndarray, shape (N,N)
        Resistance, capacitance, inductance matrices.
    """
    eps0 = 1.0 / (4.0 * np.pi * 9e9)
    muy0 = 4.0 * np.pi * 1e-7
    k_eps = (eps - 1.0) / (eps + 1.0)

    N = x.shape[0]
    R = np.zeros((N, N))
    P = np.zeros((N, N))
    L = np.zeros((N, N))

    for i in range(N):
        li = abs(x[i,1]-x[i,0]) + abs(y[i,1]-y[i,0]) + abs(z[i,1]-z[i,0])
        Ii_i = 2*li*(np.log(2*li/r[i]) - 1)

        if d[i] == 3:  # z-direction
            zim = image_locating(z[i,:], depth)
            Ii_ii = line_geometic_factor(zim[0], zim[1], z[i,0], z[i,1])
        elif d[i] == 2:  # y-direction
            Ii_ii = parallel_geometic_factor(2*depth, y[i,0], y[i,1], y[i,0], y[i,1])
        else:  # x-direction
            Ii_ii = parallel_geometic_factor(2*depth, x[i,0], x[i,1], x[i,0], x[i,1])

        R[i,i] = res/(4*np.pi*li)*(Ii_i+Ii_ii)
        P[i,i] = 1.0/(eps*eps0*4*np.pi*li)*(Ii_i+k_eps*Ii_ii)
        L[i,i] = muy0/(4*np.pi*li)*Ii_i

        for j in range(N):
            if j == i: continue
            if d[i] != d[j]:
                x1,x2,yb,xb,y1,y2,dij = input_perpendicular_case(x[i,:],y[i,:],z[i,:],d[i],
                                                                 x[j,:],y[j,:],z[j,:],d[j])
                Ii_j = perpendicular_geometic_factor(x1,x2,yb,xb,y1,y2,dij)
                zim = image_locating(z[j,:], depth)
                x1,x2,yb,xb,y1,y2,dij = input_perpendicular_case(x[i,:],y[i,:],z[i,:],d[i],
                                                                 x[j,:],y[j,:],zim,d[j])
                Ii_jj = perpendicular_geometic_factor(x1,x2,yb,xb,y1,y2,dij)
                R[i,j] = res/(4*np.pi*li)*(Ii_j+Ii_jj)
                P[i,j] = 1.0/(4*np.pi*eps*eps0*li)*(Ii_j+k_eps*Ii_jj)
            else:
                if d[i] == 1:  # x
                    dij = np.sqrt((y[i,0]-y[j,0])**2+(z[i,0]-z[j,0])**2)
                    zim = image_locating(z[j,:], depth)
                    dijj = np.sqrt((y[i,0]-y[j,0])**2+(z[i,0]-zim[0])**2)
                    if dij != 0:
                        Ii_j = parallel_geometic_factor(dij,x[i,0],x[i,1],x[j,0],x[j,1])
                        Ii_jj = parallel_geometic_factor(dijj,x[i,0],x[i,1],x[j,0],x[j,1])
                    else:
                        Ii_j = line_geometic_factor(x[i,0],x[i,1],x[j,0],x[j,1])
                        Ii_jj = parallel_geometic_factor(dijj,x[i,0],x[i,1],x[j,0],x[j,1])
                elif d[i] == 2:  # y
                    dij = np.sqrt((x[i,0]-x[j,0])**2+(z[i,0]-z[j,0])**2)
                    zim = image_locating(z[j,:], depth)
                    dijj = np.sqrt((x[i,0]-x[j,0])**2+(z[i,0]-zim[0])**2)
                    if dij != 0:
                        Ii_j = parallel_geometic_factor(dij,y[i,0],y[i,1],y[j,0],y[j,1])
                        Ii_jj = parallel_geometic_factor(dijj,y[i,0],y[i,1],y[j,0],y[j,1])
                    else:
                        Ii_j = line_geometic_factor(y[i,0],y[i,1],y[j,0],y[j,1])
                        Ii_jj = parallel_geometic_factor(dijj,y[i,0],y[i,1],y[j,0],y[j,1])
                else:  # z
                    dij = np.sqrt((y[i,0]-y[j,0])**2+(x[i,0]-x[j,0])**2)
                    zim = image_locating(z[j,:], depth)
                    if dij != 0:
                        Ii_j = parallel_geometic_factor(dij,z[i,0],z[i,1],z[j,0],z[j,1])
                        Ii_jj = parallel_geometic_factor(dij,z[i,0],z[i,1],zim[0],zim[1])
                    else:
                        Ii_j = line_geometic_factor(z[i,0],z[i,1],z[j,0],z[j,1])
                        Ii_jj = line_geometic_factor(z[i,0],z[i,1],zim[0],zim[1])
                R[i,j] = res/(4*np.pi*li)*(Ii_j+Ii_jj)
                P[i,j] = 1.0/(4*np.pi*eps*eps0*li)*(Ii_j+k_eps*Ii_jj)
                L[i,j] = muy0/(4*np.pi*li)*Ii_j

    return R, P, L
