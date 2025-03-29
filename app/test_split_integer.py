from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    # sum == value
    assert sum(split_integer(5, 3)) == 5


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    # if value divisible each value ==  to other value
    assert split_integer(9, 3) == [3, 3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    # return == value if parts = 1
    assert split_integer(100, 1) == [100]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    # if parts aren't equal, sort min -> max
    assert split_integer(10, 3) == [3, 3, 4]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    # value < number_of_parts -> parts.append(0)
    assert split_integer(3, 4) == [0, 1, 1, 1]
