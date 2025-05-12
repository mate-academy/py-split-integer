def split_integer(value: int, number_of_parts: int) -> list:
    parts = []
    if number_of_parts <= 0:
        raise ValueError("Number of parts must be greater than zero.")
    base_part = value // number_of_parts
    remainder = value % number_of_parts
    parts = [base_part] * number_of_parts
    for i in range(remainder):
        parts[i] += 1
    return parts
