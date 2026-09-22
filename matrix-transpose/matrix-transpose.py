import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    
    if not A or not A[0]:
        return []

    row = len(A)
    col = len(A[0])

    returned = []
    for j in range(col):
        upcoming_row = []
        for i in range(row):
            upcoming_row.append(A[i][j])
        returned.append(upcoming_row)
    return np.array(returned)
        
    
    