def split_integer(value: int, number_of_parts: int) -> list:
    parts = []
    for parts_left in range(number_of_parts, 0, -1):
        next_number = value // number_of_parts
        remainder = value % number_of_parts
        parts = [next_number] * number_of_parts
        for part in range(remainder):
            parts[part] += 1

    return sorted(parts)
