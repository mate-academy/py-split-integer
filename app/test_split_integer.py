from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    number_of_parts = 4
    assert sum(split_integer(value, number_of_parts)) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    number_of_parts = 2
    list_of_parts = split_integer(value, number_of_parts)
    assert list_of_parts == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1
    list_of_parts = split_integer(value, number_of_parts)
    assert len(list_of_parts) == 1 and list_of_parts[0] == value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 32
    number_of_parts = 6
    list_of_parts = split_integer(value, number_of_parts)
    sorted_list = sorted(list_of_parts)
    assert list_of_parts == sorted_list


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 3
    number_of_parts = 5
    list_of_parts = split_integer(value, number_of_parts)
    q_of_zeroes = number_of_parts - value
    assert q_of_zeroes == list_of_parts.count(0)
