from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(17, 4)
    assert sum(result) == 17, (f"Sum of parts "
                               f"({sum(result)}) "
                               f"should be equal to value")


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(12, 4)
    assert result == [3, 3, 3, 3], f"Expected [3, 3, 3, 3], got {result}"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(12, 1)
    assert result == [12], f"Expected [12], got {result}"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(13, 5)
    assert result == [2, 2, 3, 3, 3], f"List is not sorted: {result}"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(3, 4)
    assert result == [0, 1, 1, 1], f"Expected [0, 1, 1, 1], got {result}"
