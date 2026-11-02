def split_integer(value: int, number_of_parts: int) -> list[int]:
    base, remainder = divmod(value, number_of_parts)
    parts = [base] * (number_of_parts - remainder)
    parts += [base + 1] * remainder
    return parts
