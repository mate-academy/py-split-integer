def split_integer(value: int, number_of_parts: int) -> list:

    if number_of_parts == 0:
        return []
    base_value = value // number_of_parts
    remainder = value % number_of_parts
    result = [base_value] * number_of_parts
    for i in range(number_of_parts - remainder, number_of_parts):
        result[i] += 1
    return result
