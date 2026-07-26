from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert len(split_integer(12, 4)) == 4
    assert sum(split_integer(12, 4)) == 12


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(12, 4) == [3, 3, 3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(12, 1) == [12]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(7, 3) == [2, 2, 3]
    assert split_integer(10, 3) == [3, 3, 4]
    assert split_integer(8, 3) == [2, 3, 3]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(0, 4) == [0, 0, 0, 0]
    assert sum(split_integer(0, 4)) == 0


def test_required_case_17_4() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_required_case_32_6() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
