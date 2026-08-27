from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    number_of_parts = 4

    result = split_integer(value, number_of_parts)

    assert sum(result) == value, (
        "The sum of all parts should be equal to the original value"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    number_of_parts = 2

    result = split_integer(value, number_of_parts)

    assert result == [3, 3], (
        "Value should be split into equal parts when it is divisible "
        "by the number of parts"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 6
    number_of_parts = 1

    result = split_integer(value, number_of_parts)

    assert result == [6], (
        "Splitting into one part should return the original value"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    number_of_parts = 4

    result = split_integer(value, number_of_parts)

    assert result == sorted(result), (
        "Parts should be sorted in ascending order"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    number_of_parts = 3

    result = split_integer(value, number_of_parts)

    assert result == [0, 1, 1], (
        "Zeros should be added when value is less than number of parts"
    )


def test_difference_between_max_and_min_should_not_be_greater_than_one() \
        -> None:
    value = 32
    number_of_parts = 6

    result = split_integer(value, number_of_parts)

    assert max(result) - min(result) <= 1, (
        "Difference between the largest and smallest parts "
        "should not be greater than one"
    )


def test_should_return_correct_number_of_parts() -> None:
    value = 17
    number_of_parts = 4

    result = split_integer(value, number_of_parts)

    assert len(result) == number_of_parts, (
        "The result should contain the requested number of parts"
    )
