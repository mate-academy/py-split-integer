def split_integer(value: int, number_of_parts: int) -> list:
    parts = [value // number_of_parts] * number_of_parts
    for i in range(value % number_of_parts):
        parts[i] += 1
    return sorted(parts)
