from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(part for part in split_integer(32, 6)) == 32


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    number_of_parts = 2
    if value / number_of_parts == value // number_of_parts:
        assert len(set(split_integer(value, number_of_parts))) == 1


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    assert split_integer(value, 1) == [value]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    sorted_list = split_integer(17, 4)
    sorted_list.sort()
    assert split_integer(17, 4) == sorted_list


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 1
    number_of_parts = 2
    assert split_integer(value, number_of_parts) == [0, value]
