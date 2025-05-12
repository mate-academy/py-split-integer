def split_integer(value: int, number_of_parts: int) -> list:
    parts = []
    if number_of_parts <= 0:
        raise ValueError("Number of parts must be greater than zero.")
    base_part = value // number_of_parts
    remainder = value % number_of_parts
    parts = [base_part + 1] * remainder + [base_part] * (number_of_parts - remainder)
    return parts
