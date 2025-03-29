from app.split_integer import split_integer


def test_valid_value_in_split_array() -> None:
    value = 6
    number_of_parts = 2

    assert sum(split_integer(value, number_of_parts)) == value


def test_valid_dividing_by_parts() -> None:
    value = 6
    number_of_parts = 2

    assert len(split_integer(value, number_of_parts)) == number_of_parts


def test_split_into_one_part() -> None:
    value = 77
    number_of_parts = 1

    splits_result = split_integer(value, number_of_parts)

    assert splits_result[0] == value


def test_sorted_parts() -> None:
    value = 32
    number_of_parts = 6

    assert split_integer(value, number_of_parts) == [5, 5, 5, 5, 6, 6]


def test_value_less_number_of_parts() -> None:
    value = 0
    number_of_parts = 2

    assert split_integer(value, number_of_parts) == [0, 0]
