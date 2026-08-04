def split_integer(value: int, number_of_parts: int) -> list[int]:
    base = value // number_of_parts
    remainder = value % number_of_parts

    result = [base] * number_of_parts
    for i in range(remainder):
        result[i] += 1

    return sorted(result)
