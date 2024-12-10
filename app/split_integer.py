def split_integer(value: int, number_of_parts: int) -> list:
    """
    Splits the integer `value` into `number_of_parts` parts such that the difference
    between the max and min value is at most 1. The result is sorted ascending.

    :param value: The integer value to split.
    :param number_of_parts: The number of parts to split the value into.
    :return: A list of integers where the difference between max and min is <= 1.
    """
    # Base division to ensure equal distribution
    quotient = value // number_of_parts
    remainder = value % number_of_parts

    # Create the list with the base quotient and add +1 to the remainder items
    result = [quotient] * (number_of_parts - remainder) + [quotient + 1] * remainder
    result.sort()  # Ensure the result is sorted in ascending order

    return result
