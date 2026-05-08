import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    # Number of rows and columns
    rows = len(A)
    cols = len(A[0])

    # Create transpose matrix
    transpose = np.empty((cols, rows), dtype=int)

    # Swap rows and columns
    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = A[i][j]

    return transpose
