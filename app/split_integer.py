def split_integer(value: int, number_of_parts: int) -> list:
    if value < number_of_parts:
        parts = [0] * (number_of_parts - value) + [1] * value
    else:
        base = value // number_of_parts
        remainder = value % number_of_parts
        parts = [base] * number_of_parts

        for i in range(remainder):
            parts[i] += 1

    return sorted(parts)
