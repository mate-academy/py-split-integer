def split_integer(value: int, number_of_parts: int) -> list:
    base_value = value // number_of_parts
    extra_parts = value % number_of_parts
    result = [base_value] * number_of_parts

    for i in range(extra_parts):
        result[i] += 1

    result.sort()
    return result

# def split_integer(value: int, number_of_parts: int) -> list:
#     parts = []
#     for parts_left in range(number_of_parts, 0, -1):
#         next_number = value // parts_left
#         parts.append(value // parts_left)
#         value -= next_number
#     return parts
