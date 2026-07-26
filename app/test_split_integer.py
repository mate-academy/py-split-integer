from app.split_integer import split_integer


def test_sum_of_parts_is_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(32, 6)) == 32


def test_difference_between_max_and_min_is_less_or_equal_to_one() -> None:
    assert max(split_integer(17, 4)) - min(split_integer(17, 4)) <= 1
    assert max(split_integer(100, 3)) - min(split_integer(100, 3)) <= 1


def test_result_length_is_equal_to_number_of_parts() -> None:
    assert len(split_integer(8, 1)) == 1
    assert len(split_integer(20, 5)) == 5


def test_parts_are_sorted_as_ascending() -> None:
    assert split_integer(32, 6) == sorted(split_integer(32, 6))


def test_returns_equal_parts_when_divisible() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(10, 5) == [2, 2, 2, 2, 2]
