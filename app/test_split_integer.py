from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(17, 4)
    assert sum(result) == 17


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(20, 4)
    assert result == [5, 5, 5, 5]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(8, 1)
    assert result == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(32, 6)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(3, 5)
    assert result == [0, 0, 1, 1, 1]  # Sorted,
    # sum = 3, parts = 5, difference <= 1
