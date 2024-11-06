def split_integer(value: int, number_of_parts: int) -> list:
    parts = []
    if value < number_of_parts:
        parts = [0] * (number_of_parts - 1)
        parts.append(value)
        return parts
    for parts_left in range(number_of_parts, 0, -1):
        next_number = value // parts_left
        parts.append(value // parts_left)
        value -= next_number
    return parts
