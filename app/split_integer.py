def split_integer(value: int, number_of_parts: int) -> list:
    result_list = [value // number_of_parts] * number_of_parts
    for i in range(value % number_of_parts):
        result_list[-1 - i] += 1
    return result_list
