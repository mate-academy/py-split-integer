def split_integer(value: int, number_of_parts: int) -> list[int]:
    quotient, remainder = divmod(value, number_of_parts)
    return (
        [quotient] * (number_of_parts - remainder)
        + [quotient + 1] * remainder
    )
