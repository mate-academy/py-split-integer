from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    splited_integer = split_integer(8, 1)
    assert sum(splited_integer) == 8


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    splited_integer = split_integer(6, 2)
    assert splited_integer[0] == splited_integer[1]

def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    splited_integer = split_integer(17, 1)
    assert splited_integer[0] == 17


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    splited_integer = split_integer(32, 6)
    sorted_splited_integer = sorted(splited_integer)
    assert sorted_splited_integer == splited_integer


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    splited_integer = split_integer(1, 2)
    assert splited_integer == [5, 5]

