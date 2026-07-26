from typing import List


def split_integer(value: int, number_of_parts: int) -> List[int]:
    min_value = value // number_of_parts
    remainder = value % number_of_parts
    parts = [min_value] * number_of_parts

    for i in range(remainder):
        parts[i] += 1

    return sorted(parts)
