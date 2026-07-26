def split_integer(value: int, number_of_parts: int) -> list:
    """
    Розділяє ціле число на задану кількість частин.
    Залишок розподіляється рівномірно між останніми елементами.
    """
    if number_of_parts == 0:
        return []

    base_part = value // number_of_parts

    remainder = value % number_of_parts

    result = [base_part] * number_of_parts

    for i in range(remainder):
        result[-(i + 1)] += 1

    return result
