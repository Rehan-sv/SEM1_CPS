import numpy as np
import mylib  # Importing your 12-function library

def run_case_study():
    print("=== CASE STUDY: NUMPY 12-FUNCTION ANALYSIS ===\n")

    # --- GROUP 1: CREATION & STRUCTURE ---
    print("--- 1. Structure & Manipulation ---")
    
    # 1. EYE
    identity = mylib.eye(3)
    print(f"1. Identity Matrix (Eye):\n{identity}")
    
    # 2. FLIPLR
    print(f"\n2. Flipped Left-Right:\n{mylib.fliplr(identity)}")
    
    # 3. RAVEL
    print(f"\n3. Flattened (Ravel):\n{mylib.ravel(identity)}")
    
    # 4. VSTACK (Stacking two identities)
    stacked = mylib.vstack((identity, identity))
    print(f"\n4. Vertically Stacked:\n{stacked}")


    # --- GROUP 2: LOGIC & MODULARITY ---
    print("\n--- 2. Logic & Modularity ---")
    
    # 5 & 6. TRI / TRIU
    ones = np.ones((3,3))
    upper = mylib.triu(ones)
    print(f"5/6. Upper Triangle (Modular Reuse):\n{upper}")
    
    # 7. CLIP (Limiting values)
    data = np.array([-5, 0, 5, 10, 15])
    clipped = mylib.clip(data, 0, 10)
    print(f"\n7. Clipped Data (0 to 10):\n{clipped}")


    # --- GROUP 3: STATS & SEARCH ---
    print("\n--- 3. Statistics & Search ---")
    
    stats_data = np.array([[10, 20], [30, 40]])
    print(f"Data:\n{stats_data}")
    
    # 8. SUM
    print(f"8. Sum: {mylib.sum_wrapper(stats_data)}")
    
    # 9. MEAN
    print(f"9. Mean: {mylib.mean_wrapper(stats_data)}")
    
    # 10. DIAG
    print(f"10. Diagonal: {mylib.diag(stats_data)}")
    
    # 11. PTP (Range)
    print(f"11. Peak-to-Peak (Range): {mylib.ptp(stats_data)}")
    
    # 12. ARGMAX (Index of max value 40)
    flat_index = mylib.argmax(stats_data)
    print(f"12. Index of Max Value: {flat_index}")


    # --- FILE OPERATIONS ---
    print("\n--- 4. File I/O (Persistence) ---")
    filename = "case_study_data.txt"
    np.savetxt(filename, stacked, fmt='%d')
    print(f"Data saved to {filename}")
    print("Reading back...")
    print(np.loadtxt(filename))

if __name__ == "main_":
    run_case_study()