def split_integer(value: int, number_of_parts: int) -> list[int]:
    base = value // number_of_parts
    remainder = value % number_of_parts

    parts = [base] * number_of_parts
    for i in range(number_of_parts - remainder, number_of_parts):
        parts[i] += 1

    return parts
