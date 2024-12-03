def split_integer(value: int, number_of_parts: int) -> list:
    if number_of_parts == 0:
        raise ValueError("number_of_parts cannot be zero")
    if value < number_of_parts:
        raise ValueError("value cannot be less than number_of_parts")

    base = value // number_of_parts
    remainder = value % number_of_parts
    res = [base + 1 if i < remainder else base for i in range(number_of_parts)]
    return sorted(res)
