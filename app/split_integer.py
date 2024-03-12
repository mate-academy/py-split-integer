def split_integer(value: int, number_of_parts: int) -> list:
    parts = []
    for parts_left in range(number_of_parts, 0, -1):
        next_number = value // parts_left
        parts.append(next_number)
        value -= next_number
    for _ in range(number_of_parts - len(parts)):
        parts.append(0)
    return parts
