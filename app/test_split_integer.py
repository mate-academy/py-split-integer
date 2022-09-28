from app.split_integer import split_integer
import pytest


@pytest.mark.parametrize(
    "value,number_of_parts,expected",
    [
        pytest.param(
            8,
            1,
            [8],
            id="When value == 8 and number_of_parts == 1 "
               "we expect [8]"
        ),
        pytest.param(
            6,
            2,
            [3, 3],
            id="When value == 6 and number_of_parts == 2 "
               "we expect [3, 3]"
        ),
        pytest.param(
            17,
            4,
            [4, 4, 4, 5],
            id="When value == 17 and number_of_parts == 4 "
               "we expect [4, 4, 4, 5]"
        ),
        pytest.param(
            32,
            6,
            [5, 5, 5, 5, 6, 6],
            id="When value == 32 and number_of_parts == 6 "
               "we expect [5, 5, 5, 5, 6, 6]"
        )
    ]
)
def test_correct_function_work(value, number_of_parts, expected):
    assert split_integer(value, number_of_parts) == expected


def test_sum_or_the_parts_should_be_equal_to_value():
    assert sum(split_integer(8, 5)) == 8


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    assert split_integer(8, 4) == [2, 2, 2, 2]


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    assert split_integer(8, 1) == [8]


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    assert 0 in split_integer(7, 9)


def test_parts_should_be_sorted_when_they_are_not_equal():
    assert split_integer(9, 2) == sorted(split_integer(9, 2))
