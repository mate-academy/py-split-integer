def split_integer(value: int, number_of_parts: int) -> list:
    parts = []
    if number_of_parts <= 0:
        raise ValueError("Number of parts must be greater than zero.")
    for parts_left in range(number_of_parts, 0, -1):
        next_number = value // parts_left
        parts.append(value // parts_left)
        value -= next_number
    return parts
