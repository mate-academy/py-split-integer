from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    splitted_integer = split_integer(17, 4)
    assert sum(splitted_integer) == 17


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    splitted_integer = split_integer(16, 4)
    assert all(part == splitted_integer[0] for part in splitted_integer)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    splitted_integer = split_integer(8, 1)
    assert (len(splitted_integer) == 1 and splitted_integer[0] == 8)


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    splitted_integer = split_integer(17, 4)
    assert splitted_integer == sorted(splitted_integer)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    splitted_integer = split_integer(3, 5)
    assert splitted_integer == [0, 0, 1, 1, 1]
