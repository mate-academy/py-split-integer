from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    parts = split_integer(32, 6)

    assert sum(parts) == 32


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    parts = split_integer(20, 2)

    assert parts == [10, 10]


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    parts = split_integer(8, 1)

    assert parts == [8]


def test_parts_should_be_sorted_when_they_are_not_equal():
    parts = split_integer(17, 4)

    assert parts == sorted(parts)


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    parts = split_integer(1, 2)

    assert parts == [0, 1]
