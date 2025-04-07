def split_integer(value: int, number_of_parts: int) -> list:
    base_number = value // number_of_parts
    remainder = value % number_of_parts
    parts = ([base_number] * (number_of_parts - remainder)
             + [base_number + 1] * remainder)
    return parts
