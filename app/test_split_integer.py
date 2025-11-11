from app.split_integer import split_integer


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_parts_should_be_sorted_and_difference_not_more_than_one() -> None:
    result = split_integer(17, 4)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    assert sum(result) == 17


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(32, 6)
    assert sum(result) == 32


def test_should_handle_case_with_many_parts() -> None:
    result = split_integer(32, 6)
    assert len(result) == 6
