def split_integer(value: int, number_of_parts: int) -> list[int]:
    base: int = value // number_of_parts
    remainder: int = value % number_of_parts
    parts: list[int] = [base] * number_of_parts
    for i in range(remainder):
        parts[number_of_parts - 1 - i] += 1
    return parts
