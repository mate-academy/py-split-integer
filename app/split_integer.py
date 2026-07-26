def split_integer(value: int, number_of_parts: int) -> list[int]:
    """Split integer value into nearly equal integer parts.

    The result list contains exactly `number_of_parts` elements,
    where the difference between max and min values is at most 1,
    and the list is sorted in ascending order.
    """
    if number_of_parts == 1:
        return [value]

    if value < number_of_parts:
        result = [1] * value + [0] * (number_of_parts - value)
        return sorted(result)

    base = value // number_of_parts
    remainder = value % number_of_parts

    result = [base] * number_of_parts
    for i in range(remainder):
        result[-(i + 1)] += 1

    return sorted(result)
