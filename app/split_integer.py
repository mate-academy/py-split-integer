def split_integer(value: int, number_of_parts: int) -> list:
    base_part = value // number_of_parts
    remaining = value % number_of_parts

    parts = [base_part] * number_of_parts

    for i in range(remaining):
        parts[i] += 1

    parts.sort()

    return parts
