from app import split_integer


def test_should_return_same_value_when_split_into_one_part() -> None:
    assert split_integer.split_integer(8, 1) == [8]


def test_should_return_one_when_value_and_parts_are_one() -> None:
    assert split_integer.split_integer(1, 1) == [1]


def test_should_split_into_equal_parts_when_value_divides_evenly() -> None:
    assert split_integer.split_integer(6, 2) == [3, 3]


def test_should_add_one_to_last_part_when_remainder_is_one() -> None:
    assert split_integer.split_integer(17, 4) == [4, 4, 4, 5]


def test_should_sort_parts_ascending_when_remainder_is_more_than_one() -> None:
    assert split_integer.split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_return_ones_when_value_equals_number_of_parts() -> None:
    assert split_integer.split_integer(5, 5) == [1, 1, 1, 1, 1]


def test_should_return_zeros_first_when_value_is_less_than_number_of_parts(
) -> None:
    assert split_integer.split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_should_split_small_value_with_remainder_correctly() -> None:
    assert split_integer.split_integer(7, 3) == [2, 2, 3]


def test_should_split_large_value_with_remainder_correctly() -> None:
    assert split_integer.split_integer(100, 7) == [14, 14, 14, 14, 14, 15, 15]


def test_should_return_list_with_exactly_number_of_parts_elements() -> None:
    assert len(split_integer.split_integer(50, 8)) == 8
