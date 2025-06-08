def split_integer(value: int, number_of_parts: int) -> list:
    parts = []
    for parts_left in range(number_of_parts, 0, -1):
        if value < number_of_parts:
            parts.append(0)
        if value >= number_of_parts:
            next_number = value // parts_left
            parts.append(value // parts_left)
            value -= next_number
    return parts
