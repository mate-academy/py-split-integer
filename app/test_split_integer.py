from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result_function = split_integer(17, 4)
    actual = sum(result_function)
    expected = 17

    assert actual == expected, f"{actual} is not equal to {expected}"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    expected = [4, 4, 4, 5]

    assert split_integer(17, 4) == expected, f"{split_integer(17, 4)} is not equal to {expected}"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result_function = split_integer(8, 1)
    actual = result_function
    expected = [8]

    assert actual == expected, f"{actual} is not equal to {expected}"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result_function = split_integer(17, 4)
    actual = result_function
    expected = result_function.copy()
    expected.sort()

    assert actual == expected, f"{actual} is not equal to {expected}"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result_function = split_integer(1, 4)
    actual = result_function
    expected = [0, 0, 0, 1]

    assert actual == expected, f"{actual} is not equal to {expected}"
