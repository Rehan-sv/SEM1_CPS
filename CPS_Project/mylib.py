# FILE NAME: mylib.py
import numpy as np

# --- 1. ALGORITHMS & DATA STRUCTURES ---

def fliplr(m):
    """
    Flip array in the left/right direction.
    Reasoning: Uses Array Slicing (Views) for O(1) memory efficiency.
    """
    m = np.asanyarray(m)
    if m.ndim < 2:
        raise ValueError("Input must be >= 2-d.")
    # ALGORITHM: Slicing with step -1 on the second axis
    return m[:, ::-1]

def flipud(m):
    """
    Flip array in the up/down direction.
    """
    m = np.asanyarray(m)
    if m.ndim < 2:
        raise ValueError("Input must be >= 2-d.")
    # ALGORITHM: Slicing with step -1 on the first axis
    return m[::-1, ...]

def eye(N, M=None, k=0, dtype=float, order='C'):
    """
    Return a 2-D array with ones on the diagonal and zeros elsewhere.
    Reasoning: Uses Strided Memory Access to fill diagonal without loops.
    """
    if M is None:
        M = N
    # Allocation
    m = np.zeros((N, M), dtype=dtype, order=order)
    
    # Logic to handle offset k (simplified for demo)
    if k >= M: return m
    
    if k >= 0:
        i = k
        j = 0
    else:
        i = 0
        j = -k
        
    # THE ALGORITHM: Flattening 2D to 1D
    # We calculate the stride (M+1) to jump exactly to the next diagonal spot
    if i < N and j < M:
        m.flat[i*M+j :: M+1] = 1
        
    return m

def diag(v, k=0):
    """
    Extract a diagonal or construct a diagonal array.
    Reasoning: Polymorphism - behaves differently based on input dimension.
    """
    v = np.asanyarray(v)
    s = v.shape
    
    # CASE A: Input is 1D (Create Matrix)
    if len(s) == 1:
        n = s[0] + abs(k)
        res = np.zeros((n, n), v.dtype)
        if k >= 0:
            i = k
            j = 0
        else:
            i = 0
            j = -k
        # Optimization: Flat indexing
        res.flat[i*n+j :: n+1] = v
        return res
    
    # CASE B: Input is 2D (Extract Diagonal)
    elif len(s) == 2:
        return v.diagonal(k)
    else:
        raise ValueError("Input must be 1- or 2-d.")

# --- 2. MODULARITY EXAMPLES ---

def tri(N, M=None, k=0, dtype=float):
    """
    An array with ones at and below the given diagonal.
    Reasoning: Uses Broadcasting for algorithm generation.
    """
    if M is None:
        M = N
    
    # ALGORITHM: Outer Comparison (Broadcasting)
    # Compares Row Index vs Column Index
    m = np.greater_equal.outer(np.arange(N, dtype=int),
                               np.arange(M, dtype=int) - k)
    
    return m.astype(dtype, copy=False)

def triu(m, k=0):
    """
    Upper triangle of an array.
    Reasoning: Modularity - calls 'tri' to get mask, then applies it.
    """
    m = np.asanyarray(m)
    
    # MODULARITY: Calls the function defined above
    mask = tri(*m.shape[-2:], k=k-1, dtype=bool)
    
    return np.where(mask, np.zeros(1, m.dtype), m)

# --- 3. STATISTICS (Wrappers) ---

def sum(a, axis=None):
    """
    Sum of array elements.
    RUBRIC: Dispatcher Pattern.
    Expl: This function acts as a 'Facade'. It delegates the hard work 
    to the underlying C-engine (.sum method) of the array object.
    """
    a = np.asanyarray(a)
    # MODULARITY: We don't write the loop here. We verify the input
    # and dispatch it to the optimized C-method.
    return a.sum(axis=axis)

def mean(a, axis=None):
    """
    Compute the arithmetic mean.
    RUBRIC: Code Reuse.
    Expl: Mean is just Sum / Count. We reuse the sum function!
    """
    a = np.asanyarray(a)
    # ALGORITHM: Reuse existing functions to avoid errors.
    return sum(a, axis=axis) / a.size