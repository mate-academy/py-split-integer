from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 15
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert sum(result) == value, \
        f"Expected sum to be {value}, but got {sum(result)}."


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 12
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert all(x == result[0] for x in result), \
        f"Expected all parts to be equal, but got {result}."


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1
    result = split_integer(value, number_of_parts)
    assert result == [value], \
        f"Expected [{value}], but got {result}."


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert result == sorted(result), \
        f"Expected parts to be sorted, but got {result}."


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 5
    number_of_parts = 10
    result = split_integer(value, number_of_parts)
    assert len(result) == number_of_parts, \
        f"Expected {number_of_parts} parts, but got {len(result)}."
    assert result.count(0) == number_of_parts - (value % number_of_parts), \
        (f"Expected {number_of_parts - (value % number_of_parts)} zeros, "
         f" but got {result.count(0)}.")
    assert sum(result) == value, \
        f"Expected sum to be {value}, but got {sum(result)}."
