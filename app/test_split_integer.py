import pytest

from app.split_integer import split_integer


def test_length_should_be_equal_to_number_of_parts() -> None:
    assert len(split_integer(17, 4)) == 4, (
        "List should contain exactly 'number_of_parts' elements"
    )


def test_sum_of_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17, (
        "Sum of all parts should be equal to 'value'"
    )


def test_difference_between_max_and_min_less_or_equal_one() -> None:
    parts = split_integer(17, 4)
    assert max(parts) - min(parts) <= 1, (
        "Difference between max and min part should be <= 1"
    )


def test_parts_should_be_sorted_ascending() -> None:
    parts = split_integer(32, 6)
    assert parts == sorted(parts), (
        "Parts should be sorted from lowest to highest"
    )


def test_should_return_list_with_value_when_one_part() -> None:
    assert split_integer(8, 1) == [8], (
        "Single part should be equal to 'value' itself"
    )


def test_parts_should_be_equal_when_value_divisible() -> None:
    assert split_integer(6, 2) == [3, 3], (
        "All parts should be equal when 'value' is divisible"
    )


def test_greater_parts_should_be_at_the_end_when_not_divisible() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5], (
        "Greater parts should be placed at the end of the list"
    )


def test_should_add_zeros_when_value_less_than_number_of_parts() -> None:
    assert split_integer(2, 4) == [0, 0, 1, 1], (
        "Zeros should be added when 'value' < 'number_of_parts'"
    )


@pytest.mark.parametrize(
    "value,number_of_parts,expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (2, 4, [0, 0, 1, 1]),
    ],
    ids=[
        "one part",
        "divisible value",
        "not divisible value",
        "several greater parts",
        "value less than parts",
    ],
)
def test_split_integer_examples(
    value: int,
    number_of_parts: int,
    expected: list[int],
) -> None:
    assert split_integer(value, number_of_parts) == expected, (
        f"split_integer({value}, {number_of_parts}) "
        f"should return {expected}"
    )
