from app.split_integer import split_integer
from random import randint


def test_sum_or_the_parts_should_be_equal_to_value():
    # prime, even and odd values
    tested_values = [13, 14, 15]

    for tested_number in tested_values:

        # testing each possible splitting
        for pieces in range(1, tested_number + 1):

            splitted_number = split_integer(tested_number, pieces)
            assert sum(splitted_number) == tested_number


def test_should_split_a_number_into_equal_parts_when_value_is_divisible_by_number_of_parts():
    tested_value = 30
    # test odd, even and prime divisors
    divisors = [2, 3, 5]

    for divisor in divisors:

        splitted_number = split_integer(tested_value, divisor)
        assert all(splitted_number[0] == part for part in splitted_number)


def test_should_return_a_part_equals_to_a_value_when_slitting_into_one_part():
    tested_value = randint(2, 2**31)
    splitted_number = split_integer(tested_value, 1)

    assert splitted_number[0] == tested_value


def test_parts_should_be_sorted_when_they_are_not_equal():
    # very lazy way to generate random prime number(Fermat number)
    tested_value = 2 ** (2 ** randint(1, 4)) + 1
    number_of_parts = randint(2, tested_value - 1)

    splitted_number = split_integer(tested_value, number_of_parts)

    assert splitted_number == sorted(splitted_number)


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    tested_value = randint(2, 2**10)
    number_of_parts = randint(tested_value + 1, tested_value + 100)

    splitted_number = split_integer(tested_value, number_of_parts)

    assert not all(splitted_number)
