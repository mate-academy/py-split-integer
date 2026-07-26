from typing import List


def split_integer(
    value: int, number_of_parts: int
) -> List[int]:
    """
    Splits an integer into a specified number of parts.

    The difference between the max and min number in the result
    should be at most 1. The list is sorted in ascending order.
    """
    quotient, remainder = divmod(value, number_of_parts)

    result = (
        [quotient] * (number_of_parts - remainder)
        + [quotient + 1] * remainder
    )

    return result
