def split_integer(value: int, number_of_parts: int) -> list:
    if number_of_parts <= 0:
        raise ValueError("number_of_parts should be > 0")

    if number_of_parts == 1:
        return [value]

    if number_of_parts > value:
        return [0] * (number_of_parts - 1) + [value]

    parts = []
    for parts_left in range(number_of_parts, 0, -1):
        next_number = value // parts_left
        parts.append(next_number)
        value -= next_number
    return parts
