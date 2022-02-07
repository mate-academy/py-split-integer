from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    # prime, even and odd values
    tested_value = 13
    number_of_parts = 11
    splitted_number = split_integer(tested_value, number_of_parts)
    assert sum(splitted_number) == tested_value


def test_should_split_a_number_into_equal_parts_when_value_is_divisible_by_number_of_parts():
    tested_value = 30
    divisor = 3

    splitted_number = split_integer(tested_value, divisor)
    assert all(splitted_number[0] == part for part in splitted_number)


def test_should_return_a_part_equals_to_a_value_when_slitting_into_one_part():
    tested_value = 531
    splitted_number = split_integer(tested_value, 1)
    assert splitted_number[0] == tested_value


def test_parts_should_be_sorted_when_they_are_not_equal():
    tested_value = 13
    number_of_parts = 7
    splitted_number = split_integer(tested_value, number_of_parts)

    assert splitted_number == sorted(splitted_number)


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    tested_value = 100
    number_of_parts = 120
    splitted_number = split_integer(tested_value, number_of_parts)

    assert not all(splitted_number)
