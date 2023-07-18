from typing import List


def split_integer(value: int, number_of_parts: int) -> List[int]:
    quotient, remainder = divmod(value, number_of_parts)
    return [quotient + 1] * remainder + [quotient] *\
        (number_of_parts - remainder)
