from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(10, 3)) == 10


def test_difference_between_max_and_min_parts() -> None:
    assert max(split_integer(10, 3)) - min(split_integer(10, 3)) <= 1


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal_17_4() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_parts_should_be_sorted_when_they_are_not_equal_32_6() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(10, 3)
    assert len(result) == 3
    assert max(result) - min(result) <= 1
    assert result == sorted(result)
