import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,parts,expected",
    [
        (17, 4, 17),
        (2, 6, 2),
        (19, 65, 19),
        (32, 6, 32)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        parts: int,
        expected: int) -> None:
    assert (
        sum(split_integer(value, parts)) == expected
    ), f"Sum of split_integer({value}) must equal to {value}"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(4, 2) == [2, 2]
    )
    assert (
        split_integer(1, 1) == [1]
    )
    assert (
        split_integer(63, 7) == [9, 9, 9, 9, 9, 9, 9]
    )
    assert (
        split_integer(186, 3) == [62, 62, 62]
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (split_integer(3, 1)[0] == 3)
    assert (split_integer(10, 1)[0] == 10)
    assert (split_integer(23, 1)[0] == 23)
    assert (split_integer(1, 1)[0] == 1)


@pytest.mark.parametrize(
    "value,parts",
    [
        (17, 4),
        (17, 645),
        (12, 89),
        (765, 54)
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        parts: int) -> None:
    assert (
        split_integer(value, parts) == sorted(split_integer(value, parts))
    )


@pytest.mark.parametrize(
    "value,parts",
    [
        (1, 3),
        (3, 5),
        (7, 21),
        (43, 89)
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        parts: int) -> None:
    assert (
        sum(split_integer(value, parts)[:parts - value]) == 0
    )
