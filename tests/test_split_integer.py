from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    actual = split_integer(255, 4)
    expected = 255

    assert sum(actual) == expected


def test_should_split_a_number_into_equal_parts_when_value_is_divisible_by_number_of_parts():
    actual = split_integer(200, 4)
    expected = [50, 50, 50, 50]

    assert actual == expected


def test_should_return_a_part_equals_to_a_value_when_slitting_into_one_part():
    actual = split_integer(999, 1)
    expected = [999]

    assert actual == expected


def test_parts_should_be_sorted_when_they_are_not_equal():
    actual = split_integer(189, 8)
    expected = [23, 23, 23, 24, 24, 24, 24, 24]

    assert actual == expected


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    actual = split_integer(5, 8)
    expected = [0, 0, 0, 1, 1, 1, 1, 1]

    assert actual == expected
