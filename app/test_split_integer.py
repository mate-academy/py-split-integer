from app.split_integer import split_integer


def test_split_6_into_2_parts() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_split_17_into_4_parts() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_split_32_into_6_parts() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_should_add_zeros_when_value_is_less_than_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_result_length_equals_number_of_parts() -> None:
    result = split_integer(17, 4)
    assert len(result) == 4


def test_difference_between_parts_not_greater_than_one() -> None:
    result = split_integer(17, 4)
    assert max(result) - min(result) <= 1
