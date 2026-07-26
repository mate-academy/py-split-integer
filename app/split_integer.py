def split_integer(value: int, number_of_parts: int) -> list:
    base = value // number_of_parts
    remainder = value % number_of_parts

    parts = [base] * number_of_parts
    for i in range(remainder):
        parts[i] += 1

    return sorted(parts)