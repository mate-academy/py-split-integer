from typing import List


def split_integer(value: int, number_of_parts: int) -> List[int]:
    """
    Splits the integer `value` into `number_of_parts` parts where:
    - The difference between the max and min number in the array is <= 1
    - The array is sorted in ascending order.

    :param value: The integer value to split
    :param number_of_parts: The number of parts to split the value into
    :return: A list of integers
    """
    # Base case: if only 1 part, return the value as a list
    if number_of_parts == 1:
        return [value]
    quotient, remainder = divmod(value, number_of_parts)

    # Create a list with `quotient` as the base value
    result = ([quotient] *
              (number_of_parts - remainder) +
              [quotient + 1] * remainder)

    return result
