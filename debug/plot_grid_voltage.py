import numpy as np
import matplotlib.pyplot as plt
from load_mat import load_mat   # giả định bạn có hàm này để đọc file .mat

def plot_grid_voltage():
    """
    Load voltage results from multiple grid configurations and plot them together.
    """

    plt.figure(figsize=(8,6))

    # Grid 1x1
    tv, uv = load_mat('ket_qua_luoi_11RBF.mat', ['tv','uv'])
    plt.plot(tv*1e6, uv[0][:,0], '--r', linewidth=3, label='grid 1x1')

    # Grid 2x2
    tv, uv = load_mat('ket_qua_luoi_22RBF.mat', ['tv','uv'])
    plt.plot(tv*1e6, uv[0][:,0], '-.b', linewidth=3, label='grid 2x2')

    # Grid 6x6
    tv, uv = load_mat('ket_qua_luoi_66RBF.mat', ['tv','uv'])
    plt.plot(tv*1e6, uv[0][:,0], 'k', linewidth=3, label='grid 6x6')

    plt.xlabel('t (µs)')
    plt.ylabel('Voltage (V)')
    plt.grid(True)
    plt.legend()
    plt.title('Voltage comparison across different grounding grids')
    plt.tight_layout()
    plt.show()
