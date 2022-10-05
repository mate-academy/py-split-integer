from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    sum_integer = 0
    for parts_integ in split_integer(85, 10):
        sum_integer = sum_integer + int(parts_integ)
    assert sum_integer == 85


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert 80 % len(split_integer(80, 10)) == 0


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(1, 1) == [1]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(11, 3) == [3, 4, 4]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert int(split_integer(1, 3)[0]) == 0
