from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    parts = split_integer(90, 3)
    assert len(parts) == 3
    assert sum(parts) == 90
    assert max(parts) - min(parts) <= 1
    equal_parts = split_integer(32, 6)
    assert len(equal_parts) == 6
    assert sum(equal_parts) == 32
    assert max(equal_parts) - min(equal_parts) <= 1


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(60, 4) == [15, 15, 15, 15]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 4) == [0, 1, 1, 1]
