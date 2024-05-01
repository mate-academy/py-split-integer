from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(6, 2)) == 6


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    number_of_parts = 2
    ls = split_integer(value, number_of_parts)
    assert all(ls[i] == ls[i + 1] for i in range(len(ls) - 1)) is True


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1
    ls = split_integer(value, number_of_parts)
    assert ls == [value]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 1545
    number_of_parts = 15
    ls = split_integer(value, number_of_parts)
    assert ls == sorted(ls)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 4
    number_of_parts = 5
    ls = split_integer(value, number_of_parts)
    assert ls == [0, 1, 1, 1, 1]
