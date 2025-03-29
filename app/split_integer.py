def split_integer(value: int, number_of_parts: int) -> list:
    base_value = value // number_of_parts  # Minimum value each part gets
    remainder = value % number_of_parts  # Remaining value to be distributed

    parts = [base_value] * number_of_parts  # Start with equal distribution

    # Distribute the remainder, increasing the first 'remainder' elements
    for i in range(remainder):
        parts[i] += 1

    return sorted(parts)  # Ensure ascending order
