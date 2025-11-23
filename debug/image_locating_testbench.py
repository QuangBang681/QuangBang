import numpy as np
from image_locating import image_locating

def main():
    # Case 1: z = [1, 3], depth = 2
    z = [1, 3]
    depth = 2
    z_image = image_locating(z, depth)
    print("=== Testbench Case 1 ===")
    print(f"z={z}, depth={depth} -> z_image={z_image}")

    # Case 2: z = [0, -5], depth = 1
    z = [0, -5]
    depth = 1
    z_image = image_locating(z, depth)
    print("\n=== Testbench Case 2 ===")
    print(f"z={z}, depth={depth} -> z_image={z_image}")

    # Case 3: z = [10, 20], depth = 0.5
    z = [10, 20]
    depth = 0.5
    z_image = image_locating(z, depth)
    print("\n=== Testbench Case 3 ===")
    print(f"z={z}, depth={depth} -> z_image={z_image}")

if __name__ == "__main__":
    main()
