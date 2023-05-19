def split_integer(value: int, number_of_parts: int) -> list:
    parts = [value // number_of_parts] * number_of_parts
    remainder = value % number_of_parts
    for i in range(remainder):
        parts[i] += 1
    parts.sort()
    return parts


print(split_integer(5, 6))
