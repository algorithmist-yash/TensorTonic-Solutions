import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    # Handle empty input
    if len(seqs) == 0:
        return np.empty((0, 0), dtype=int)

    # Determine target length
    if max_len is None:
        max_len = max(len(seq) for seq in seqs) if seqs else 0

    # Create result array filled with pad_value
    result = np.full((len(seqs), max_len), pad_value, dtype=int)

    # Copy sequences with truncation if needed
    for i, seq in enumerate(seqs):
        length = min(len(seq), max_len)
        result[i, :length] = seq[:length]

    return result