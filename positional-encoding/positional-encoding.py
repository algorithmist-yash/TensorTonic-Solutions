import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    # positions: (seq_len, 1)
    positions = np.arange(seq_len)[:, np.newaxis]

    # Dimension indices for sin columns
    div_terms = np.power(
        base,
        (2 * (np.arange((d_model + 1) // 2))) / d_model
    )

    # Compute angles
    angles = positions / div_terms

    # Initialize output
    pe = np.zeros((seq_len, d_model), dtype=float)

    # Even indices -> sin
    pe[:, 0::2] = np.sin(angles)

    # Odd indices -> cos
    pe[:, 1::2] = np.cos(angles[:, :d_model // 2])

    return pe