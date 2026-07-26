def split_integer(value: int, number_of_parts: int) -> list:
    base = value // number_of_parts
    remainder = value % number_of_parts

    parts_without_remainder = number_of_parts - remainder

    return [base] * parts_without_remainder + [base + 1] * remainder
