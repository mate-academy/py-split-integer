from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(10, 3)) == 10


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(9, 3) == [3, 3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(9, 1) == [9]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(10, 3) == [3, 3, 4]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 3) == [0, 1, 1]


def test_should_contain_exactly_number_of_parts_elements() -> None:
    assert len(split_integer(9, 3)) == 3


def test_parts_difference_should_not_exceed_one() -> None:
    parts = split_integer(10, 3)  # Повертає
    difference = max(parts) - min(parts)
    assert difference <= 1
