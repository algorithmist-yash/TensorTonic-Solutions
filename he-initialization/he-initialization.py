def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    # Write code here
    limit = math.sqrt(6 / fan_in)

    result = []

    for row in W:

        new_row = []

        for val in row:

            scaled = val * (2 * limit) - limit

            new_row.append(scaled)

        result.append(new_row)

    return result