def split_integer(value: int, number_of_parts: int) -> list[int]:
    base = value // number_of_parts
    remainder = value % number_of_parts
    return [base] * (number_of_parts - remainder) + [base + 1] * remainder
