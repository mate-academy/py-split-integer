from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() \
        -> None:
    value = 17
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() \
        -> None:
    value = 8
    number_of_parts = 2
    result = split_integer(value, number_of_parts)
    expected = [4, 4]
    assert result == expected


def test_should_return_part_equals_to_value_when_split_into_one_part() \
        -> None:
    value = 10
    number_of_parts = 1
    result = split_integer(value, number_of_parts)
    expected = [10]
    assert result == expected


def test_parts_should_be_sorted_when_they_are_not_equal() \
        -> None:
    value = 9
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() \
        -> None:
    value = 3
    number_of_parts = 5
    result = split_integer(value, number_of_parts)
    expected = [0, 0, 1, 1, 1]
    assert sorted(result) == expected


def test_difference_between_max_and_min_should_be_less_than_or_equal_to_one() \
        -> None:
    value = 10
    number_of_parts = 3
    result = split_integer(value, number_of_parts)
    max_part = max(result)
    min_part = min(result)
    assert max_part - min_part <= 1


def test_should_split_into_parts_with_max_difference_one() \
        -> None:
    value = 15
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert max(result) - min(result) <= 1
