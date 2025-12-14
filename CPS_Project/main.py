import numpy as np
import mylib   # importing your custom NumPy library


def main():
    print("===== NUMPY CASE STUDY USING mylib =====\n")

    # ------------------------------------------
    # 1. CREATION & DATA STRUCTURES
    # ------------------------------------------
    print("1. CREATION & DATA STRUCTURES")

    A = mylib.eye(3)
    print("Identity Matrix:\n", A)

    B = np.array([[1, 2, 3],
                  [4, 5, 6]])
    print("\nOriginal Matrix:\n", B)

    print("Flipped Left-Right:\n", mylib.fliplr(B))
    print("Raveled Array:", mylib.ravel(B))

    C = mylib.vstack((B, B))
    print("Vertical Stack:\n", C)

    # ------------------------------------------
    # 2. LOGIC & MASKING
    # ------------------------------------------
    print("\n2. LOGIC & MASKING")

    print("Lower Triangular Mask:\n", mylib.tri(4))

    M = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
    print("Upper Triangular Matrix:\n", mylib.triu(M))

    values = np.array([-10, -3, 0, 5, 15])
    print("Clipped Values:", mylib.clip(values, 0, 10))

    # ------------------------------------------
    # 3. STATISTICS & SEARCHING
    # ------------------------------------------
    print("\n3. STATISTICS & SEARCHING")

    D = np.array([10, 20, 30, 40, 50])
    print("Array:", D)

    print("Sum:", mylib.sum_wrapper(D))
    print("Mean:", mylib.mean_wrapper(D))
    print("Peak-to-Peak:", mylib.ptp(D))
    print("Index of Max:", mylib.argmax(D))

    print("Diagonal Matrix from Vector:\n", mylib.diag(D))

