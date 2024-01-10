def split_integer(value: int, number_of_parts: int) -> list:
    parts = []
    for parts_left in range(number_of_parts, 0, -1):
        next_number = value // parts_left
        parts.append(value // parts_left)
        value -= next_number
    return parts


def split_on_different_parts(value: int, number_of_parts: int):
    result_list = [value // number_of_parts] * number_of_parts
    for i in range(value % number_of_parts):
        result_list[-1 - i] += 1
    if value % number_of_parts == 0:
        result_list[0] -= 1
        result_list[-1] += 1
    return result_list

print(split_on_different_parts(4, 1))