from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    test_parameters = (36, 5)
    expected = split_integer(*test_parameters)
    assert sum(expected) == test_parameters[0]


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    test_parameters = (36, 6)
    expected = split_integer(*test_parameters)
    assert expected.count(expected[0]) == test_parameters[1]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    test_parameters = (7, 1)
    expected = split_integer(*test_parameters)
    assert len(expected) == test_parameters[1]
    assert expected[0] == test_parameters[0]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    test_parameters = (36, 9)
    expected = split_integer(*test_parameters)
    assert expected == sorted(expected)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    test_parameters = (4, 5)
    expected = split_integer(*test_parameters)
    assert 0 in expected
