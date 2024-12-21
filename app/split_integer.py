
def split_integer(value: int, number_of_parts: int) -> list:
    parts = []
    for parts_left in range(number_of_parts, 0, -1):
        next_number = value // parts_left
        parts.append(value // parts_left)
        print(parts_left, parts, value)
        value -= next_number
        # print(value)
    return parts


split_integer(32, 33)
