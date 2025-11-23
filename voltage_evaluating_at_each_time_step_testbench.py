# voltage_evaluating_at_each_time_step_testbench.py
import numpy as np
from voltage_evaluating_at_each_time_step import voltage_evaluating_at_each_time_step

def main():
    # Setup a tiny system with 2 elements
    Nt = 5  # Nt+1 time rows
    N = 2
    dx = np.array([1.0, 0.8])

    # Element-to-node mapping (1-based). Second element has open right end (node id 0).
    element = np.array([
        [1, 2],   # element 1 between node 1 and 2
        [2, 0],   # element 2 between node 2 and open end
    ], dtype=int)

    # Node voltages (3 nodes to be safe). We'll set time-varying V externally per step.
    V = np.array([0.0, 0.0, 0.0])

    # Per-element segment counts: Ne_1=2, Ne_2=3
    Ne1, Ne2 = 2, 3

    # Initialize iv and uv lists
    iv = [
        np.zeros((Nt + 1, Ne1)),
        np.zeros((Nt + 1, Ne2)),
    ]
    uv = [
        np.zeros((Nt + 1, Ne1 + 1)),
        np.zeros((Nt + 1, Ne2 + 1)),
    ]

    # Segment parameters Gc, Cc for each element
    Gc = [
        np.array([0.1, 0.12]),            # element 1: 2 segments
        np.array([0.15, 0.16, 0.18]),     # element 2: 3 segments
    ]
    Cc = [
        np.array([2.0, 2.2]),
        np.array([1.8, 2.0, 2.1]),
    ]

    dt = 1e-9  # small time step

    # Create some simple current inputs over time
    for t in range(Nt + 1):
        iv[0][t, :] = 0.5 * t * np.array([1.0, -0.5])
        iv[1][t, :] = 0.3 * t * np.array([1.0, 0.5, -0.2])

    # Time stepping: update V, then compute uv at each t (starting from t=1 to have t-1 available)
    for t in range(1, Nt + 1):
        # Example node voltages at time t
        V[0] = 10.0 * np.sin(0.2 * t)
        V[1] = 5.0 * np.cos(0.2 * t)

        uv = voltage_evaluating_at_each_time_step(iv, uv, V, element, Gc, Cc, t, dx, dt)

    # Show results at final time
    print("=== voltage_evaluating_at_each_time_step testbench ===")
    print("Element 1 uv at final time (endpoints):", uv[0][-1, :])
    print("Element 2 uv at final time (endpoints):", uv[1][-1, :])

    # Inspect interior nodes for element 2
    print("Element 2 interior uv at final time:", uv[1][-1, 1:-1])

if __name__ == "__main__":
    main()
