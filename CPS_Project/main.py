import numpy as np

def case_study_demo():
    print("--- 1. Data Structure & Algorithms (from twodim_base) ---")
    
    # Using 'eye' - Demonstrates Strided Memory Access
    # (Explain: We create a 5x5 Identity matrix)
    identity = np.eye(5)
    print("\nIdentity Matrix (np.eye):\n", identity)

    # Using 'diag' - Demonstrates Polymorphism
    # (Explain: We extract the diagonal from the identity matrix)
    diagonal_vals = np.diag(identity)
    print("\nDiagonal Elements (np.diag):\n", diagonal_vals)

    # Using 'fliplr' - Demonstrates Memory Views (Slicing)
    # (Explain: We flip the matrix left-to-right efficiently)
    flipped = np.fliplr(identity)
    print("\nFlipped Matrix (np.fliplr):\n", flipped)

    print("\n--- 2. Modular Design (Triangle Logic) ---")
    
    # Using 'triu' - Demonstrates Modularity
    # (Explain: triu calls 'tri' internally to get a mask)
    triangle = np.triu(np.ones((4, 4)), k=0)
    print("\nUpper Triangle (np.triu):\n", triangle)

    print("\n--- 3. File Handling (The Missing Piece) ---")
    
    # Using 'savetxt' - Demonstrates File Operations
    # (Explain: Writing our array to a text file)
    filename = "output_data.txt"
    np.savetxt(filename, triangle, fmt='%d')
    print(f"Successfully wrote data to '{filename}'")

    # Prove it worked by reading it back
    loaded_data = np.loadtxt(filename)
    print("\nData read back from file:\n", loaded_data)
    # ... inside run_viva_demo() ...
    
    print("\n--- 4. Statistics (Optional Extra) ---")
    data = np.array([[1, 2], [3, 4]])
    
    # Demonstrate 'sum'
    total = mylib.sum(data)
    print(f"Sum of elements: {total}")
    
    # Demonstrate 'mean'
    average = mylib.mean(data)
    print(f"Mean of elements: {average}")

if __name__ == "__main__":
    case_study_demo()