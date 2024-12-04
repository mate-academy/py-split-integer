def split_integer(value: int, number_of_parts: int) -> list:
    parts = []
    number = value
    for parts_left in range(number_of_parts, 0, -1):
        next_number = number // parts_left
        parts.append(next_number)
        number -= next_number
    return parts

# print([32 // 6] * 6)
# print(split_integer(28, 7))
