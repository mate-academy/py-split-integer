import pytest

from app.split_integer import split_integer


def helper_asserts(
        value: int,
        number_of_parts: int,
        result: list
) -> None:
    assert sum(result) == value
    assert len(result) == number_of_parts
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    assert all(isinstance(x, int) for x in result)


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (2, 3),
        (2, 5),
    ],
)
def test_result_properties_for_various_inputs(
        value: int,
        number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    helper_asserts(value, number_of_parts, result)


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6])
    ]
)
def test_returns_expected_examples_from_spec(
        value: int,
        number_of_parts: int,
        expected: list
) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (2, 5, [0, 0, 0, 1, 1]),
    ]
)
def test_zeros_are_at_the_beginning_when_value_less_than_parts(
        value: int,
        number_of_parts: int,
        expected: list
) -> None:
    result = split_integer(value, number_of_parts)
    assert result == expected
