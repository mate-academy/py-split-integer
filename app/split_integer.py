def split_integer(value: int, number_of_parts: int) -> list:
    parts = []
    for parts_left in range(number_of_parts, 0, -1):
        next_number = value // parts_left
        parts.append(value // parts_left)
        value -= next_number
    return parts


# print(split_integer(8, 1)) #== [8]
# print(split_integer(6, 2)) #== [3, 3]
# print(split_integer(17, 4)) #== [4, 4, 4, 5]
# print(split_integer(32, 6)) #== [5, 5, 5, 5, 6, 6]

