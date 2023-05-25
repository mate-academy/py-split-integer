def split_integer(value: int, number_of_parts: int) -> list:
    parts = []
    for parts_left in range(number_of_parts, 0, -1):
        next_number = value // parts_left
        parts.append(value // parts_left)
        value -= next_number
    return parts


# print(split_integer
#     (
#     7,4
# )
# )


result = split_integer(7, 4)
sorted_list = result.copy()
sorted_list.sort()


print(result)
print(sorted_list)