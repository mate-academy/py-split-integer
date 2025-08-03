from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    number_of_parts = 4
    assert sum(split_integer(value, number_of_parts)) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    number_of_parts = 2
    if value % number_of_parts == 0:
        number = value / number_of_parts
        lst = split_integer(value, number_of_parts)
        assert all(x == number for x in lst)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1
    lst = split_integer(value, number_of_parts)
    assert len(lst) == 1 and lst[0] == value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 32
    number_of_parts = 6
    lst = split_integer(value, number_of_parts)
    assert lst == sorted(lst)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 5
    number_of_parts = 10
    lst = split_integer(value, number_of_parts)
    assert lst.count(0) == number_of_parts - value
