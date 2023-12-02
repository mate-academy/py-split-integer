def split_integer(value: int, number_of_parts: int) -> list:
    parts = []
    for parts_left in range(number_of_parts, 0, -1):
        next_number = value // parts_left
        parts.append(value // parts_left)
        value -= next_number
    return parts


print(split_integer(8, 3))


# def split_and_increment_the_last_number(value: int, number_of_parts: int):
#     result_list = [value // number_of_parts] * number_of_parts
#     if value % number_of_parts != 0:
#         result_list[-1] += 1
#     return result_list
#
#
# print(split_and_increment_the_last_number(8, 3)) #[2, 2, 3]