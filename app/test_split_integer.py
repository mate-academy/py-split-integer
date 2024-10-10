import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts,expected_result",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6])
    ],
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int,
        expected_result: list[int, ...]
) -> None:
    assert split_integer(value, number_of_parts) == expected_result

@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6)
    ],
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        number_of_parts: int
) -> None:
    assert (
        split_integer(value, number_of_parts) ==
        [value // number_of_parts] * number_of_parts
    )

@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6)
    ],
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int,
        number_of_parts: int
) -> None:
    assert split_integer(value, number_of_parts) == [value // number_of_parts]

@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6)
    ],
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int
) -> None:
    actual_result = split_integer(value, number_of_parts)
    assert actual_result == sorted(actual_result)

@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6)
    ],
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_parts: int
) -> None:
    assert (
        split_integer(value, number_of_parts) ==
        [0 if value < number_of_parts else value] * number_of_parts
    )
