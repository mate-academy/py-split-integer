from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    expected = [3, 3]
    actual = split_integer(6, 2)
    assert sum(expected) == sum(actual)


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    expected = [3, 3]
    actual = split_integer(6, 2)
    assert expected == actual


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    expected = [8]
    actual = split_integer(8, 1)
    assert expected == actual


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    expected = [4, 4, 4, 5]
    actual = split_integer(17, 4)
    assert expected == actual


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    expected = [0, 1, 1]
    actual = split_integer(2, 3)
    assert expected == actual
