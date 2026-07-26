def split_integer(value: int, number_of_parts: int) -> list:
    if value < number_of_parts:
        return [0] * (number_of_parts - 1) + [value]

    base_value = value // number_of_parts
    remainder = value % number_of_parts

    parts = [base_value] * number_of_parts
    for i in range(remainder):
        parts[i] += 1

    return sorted(parts)
