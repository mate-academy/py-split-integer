def split_integer(value: int, number_of_parts: int) -> list[int]:
    base = value // number_of_parts
    remainder = value % number_of_parts

    # start with equal base parts
    parts = [base] * number_of_parts

    # distribute remainder: add +1 to the first `remainder` parts
    for i in range(remainder):
        parts[i] += 1

    # return sorted list (smallest to largest)
    return sorted(parts)
