from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
   assert sum(split_integer(6, 2)) == 6


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 10
    number_of_parts = 5
    check_obj = value / number_of_parts
    for parts in split_integer(value, number_of_parts):
        assert parts == check_obj


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 14
    number_of_parts = 1
    assert split_integer(value, number_of_parts)[0] == value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert sorted(split_integer(20, 3)) == [6, 7, 7]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    number_of_parts = 4
    assert 0 in split_integer(value, number_of_parts)
