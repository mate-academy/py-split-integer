from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(32, 6)) == 32
    assert sum(split_integer(100, 7)) == 100


def test_difference_between_min_and_max_should_not_exceed_one() -> None:
    result = split_integer(17, 4)
    assert max(result) - min(result) <= 1


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(18, 3) == [6, 6, 6]
    assert split_integer(20, 4) == [5, 5, 5, 5]
    assert split_integer(12, 2) == [6, 6]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(170, 1) == [170]
    assert split_integer(25, 1) == [25]
    assert split_integer(1, 1) == [1]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(11, 3)
    assert result == sorted(result)
    result = split_integer(17, 4)
    assert result == sorted(result)
    result = split_integer(23, 5)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(1, 3) == [0, 0, 1]


def test_should_return_correct_number_of_parts() -> None:
    assert len(split_integer(17, 4)) == 4
    assert len(split_integer(32, 6)) == 6
    assert len(split_integer(100, 7)) == 7


def test_examples_from_task() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
