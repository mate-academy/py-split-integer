from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    for value, parts in [(10, 3), (7, 3), (11, 5), (25, 7)]:
        assert sum(split_integer(value, parts)) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(10, 5) == [2, 2, 2, 2, 2]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(10, 1) == [10]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    for value, parts in [(10, 3), (7, 3), (11, 5), (32, 6)]:
        result = split_integer(value, parts)

    assert result == sorted(result), f"Result {result} is not sorted"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(1, 5) == [0, 0, 0, 0, 1]
    assert split_integer(0, 5) == [0, 0, 0, 0, 0]


def test_difference_between_max_and_min_should_be_less_than_or_equal_to_one()\
        -> None:
    for value, parts in [(10, 3), (7, 3), (11, 5), (32, 6)]:
        result = split_integer(value, parts)
        assert max(result) - min(result) <= 1,\
            f"Max-min difference in {result} is greater than 1"
