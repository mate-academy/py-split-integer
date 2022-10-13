from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    # assert split_integer(11, 4) == [2, 3, 3, 3]
    test_parameters = (11, 4)
    expected = split_integer(*test_parameters)
    assert sum(expected) == test_parameters[0]


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    # assert split_integer(18, 3) == [6, 6, 6]
    test_parameters = (18, 3)
    expected = split_integer(*test_parameters)
    assert expected.count(expected[0]) == test_parameters[1]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    # assert split_integer(3, 1) == [3]
    test_parameters = (3, 1)
    expected = split_integer(*test_parameters)
    assert expected[0] == test_parameters[0]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    # assert split_integer(19, 3) == [6, 6, 7]
    test_parameters = (19, 3)
    expected = split_integer(*test_parameters)
    assert expected == sorted(expected)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    # assert split_integer(4, 5) == [0, 1, 1, 1, 1]
    test_parameters = (4, 5)
    expected = split_integer(*test_parameters)
    assert 0 in expected


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    # assert split_integer(4, 5) == [0, 1, 1, 1, 1]
    test_parameters = (4, 5)
    expected = split_integer(*test_parameters)
    assert 0 in expected


def test_should_difference_between_numbers_le_than_one() -> None:
    # assert split_integer(13, 4) == [3, 3, 3, 4]
    test_parameters = (13, 4)
    expected = split_integer(*test_parameters)
    assert max(expected) - min(expected) == 1
