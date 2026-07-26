from app.split_integer import split_integer


def test_returns_correct_number_of_parts() -> None:
    assert len(split_integer(10, 3)) == 3


def test_sum_of_parts_equals_value() -> None:
    assert sum(split_integer(17, 4)) == 17


def test_result_is_sorted_ascending() -> None:
    assert split_integer(32, 6) == sorted(split_integer(32, 6))


def test_max_min_difference_not_more_than_one() -> None:
    assert max(split_integer(32, 6)) - min(split_integer(32, 6)) <= 1


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(12, 3) == [4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_examples_from_task() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_value_equals_parts_returns_ones() -> None:
    assert split_integer(7, 7) == [1] * 7
