# def split_integer(value: int, number_of_parts: int) -> list:
#     parts = []
#     for parts_left in range(number_of_parts, 0, -1):
#         next_number = value // parts_left
#         parts.append(value // parts_left)
#         value -= next_number
#     return parts
def split_integer(value: int, number_of_parts: int) -> list:
    parts = []
    for parts_left in range(min(value, number_of_parts), 0, -1):
        next_number = value // parts_left
        parts.append(next_number)
        value -= next_number
    parts += [0] * (number_of_parts - len(parts))
    return parts
