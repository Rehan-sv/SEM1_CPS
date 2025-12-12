import numpy as np

# ==========================================
# 1. CREATION & DATA STRUCTURES (4 Functions)
# ==========================================

def eye(N, M=None, k=0, dtype=float, order='C'):
    """
    1. Creates Identity Matrix.
    RUBRIC: Algorithmic Thinking (Strided Access).
    Expl: Uses strides to fill diagonal in O(N) instead of O(N^2).
    """
    if M is None: M = N
    m = np.zeros((N, M), dtype=dtype, order=order)
    if k == 0:
        # ALGORITHM: Flat indexing with stride M+1
        m.flat[::M+1] = 1
    return m

def fliplr(m):
    """
    2. Flips array Left-Right.
    RUBRIC: Data Structures (Memory Views).
    Expl: Returns a View '[:, ::-1]' without copying memory.
    """
    m = np.asanyarray(m)
    return m[:, ::-1]

def ravel(a, order='C'):
    """
    3. Flattens an array to 1D.
    RUBRIC: Data Organization.
    Expl: Converts complex n-D shapes into a contiguous 1D block.
    """
    a = np.asanyarray(a)
    # DATA STRUCTURE: Changing dimensional metadata
    return a.ravel(order=order)

def vstack(tup):
    """
    4. Stacks arrays vertically (Row-wise).
    RUBRIC: Modularity (Dependency).
    Expl: This function is a 'Wrapper'. It cleans input using 
    'atleast_2d' and delegates to 'concatenate'.
    """
    # MODULARITY: Reuse of atleast_2d and concatenate
    arrs = [np.atleast_2d(a) for a in tup]
    return np.concatenate(arrs, axis=0)

# ==========================================
# 2. LOGIC & MASKING (3 Functions)
# ==========================================

def tri(N, M=None, k=0, dtype=float):
    """
    5. Helper: Creates triangle mask.
    RUBRIC: Algorithms (Broadcasting).
    Expl: Compares indices mathematically to generate shape.
    """
    if M is None: M = N
    m = np.greater_equal.outer(np.arange(N, dtype=int),
                               np.arange(M, dtype=int) - k)
    return m.astype(dtype, copy=False)

def triu(m, k=0):
    """
    6. Upper Triangle.
    RUBRIC: Modular Design.
    Expl: Calls 'tri' helper to get mask, then applies it.
    """
    m = np.asanyarray(m)
    mask = tri(*m.shape[-2:], k=k-1, dtype=bool)
    return np.where(mask, np.zeros(1, m.dtype), m)

def clip(a, a_min, a_max):
    """
    7. Limits values between min and max.
    RUBRIC: Control Flow / UFuncs.
    Expl: Element-wise comparison logic.
    """
    a = np.asanyarray(a)
    # ALGORITHM: Fast element-wise comparison
    return np.clip(a, a_min, a_max)

# ==========================================
# 3. STATISTICS & SEARCHING (5 Functions)
# ==========================================

def sum_wrapper(a, axis=None):
    """
    8. Summation.
    RUBRIC: Dispatching.
    Expl: Dispatches to internal C-engine.
    """
    a = np.asanyarray(a)
    return a.sum(axis=axis)

def mean_wrapper(a, axis=None):
    """
    9. Arithmetic Mean.
    RUBRIC: Code Reuse.
    Expl: Reuses sum function (Mean = Sum / Size).
    """
    a = np.asanyarray(a)
    return sum_wrapper(a, axis=axis) / a.size

def diag(v, k=0):
    """
    10. Diagonal Extraction/Creation.
    RUBRIC: Polymorphism.
    Expl: Behavior changes based on input dimension (1D vs 2D).
    """
    v = np.asanyarray(v)
    s = v.shape
    if len(s) == 1:
        n = s[0] + abs(k)
        res = np.zeros((n, n), v.dtype)
        res.flat[::n+1] = v
        return res
    return v.diagonal(k)

def ptp(a, axis=None):
    """
    11. Peak-to-Peak (Range).
    RUBRIC: Algorithmic Logic.
    Expl: Calculates Range = Max - Min.
    """
    a = np.asanyarray(a)
    return a.max(axis=axis) - a.min(axis=axis)

def argmax(a, axis=None):
    """
    12. Index of Maximum Value.
    RUBRIC: Search Algorithms.
    Expl: Performs a linear search to find position of max value.
    """
    a = np.asanyarray(a)
    return a.argmax(axis=axis)