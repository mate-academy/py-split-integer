"""Split an integer into nearly equal ascending integer parts."""

from typing import List


def split_integer(value: int, number_of_parts: int) -> List[int]:
    """
    Return a list of `number_of_parts` integers that sums to `value`.

    The list is sorted ascending and the difference between max and min
    is at most 1.
    """
    base = value // number_of_parts
    remainder = value % number_of_parts
    # ex.: value=17, parts=4 -> [4, 4, 4, 5]
    return [base] * (number_of_parts - remainder) + [base + 1] * remainder
