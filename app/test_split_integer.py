import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (5, 5, [1, 1, 1, 1, 1]),
        (10, 3, [3, 3, 4]),
    ],
)
def test_split_integer_expected_results(
    value: int, number_of_parts: int, expected: list[int]
) -> None:
    """Testa se a funcao retorna os valores esperados."""
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (10, 1),
        (15, 3),
        (22, 5),
        (100, 13),
        (7, 4),
    ],
)
def test_split_integer_properties(
    value: int, number_of_parts: int
) -> None:
    """Testa se o resultado atende as restricoes."""
    result = split_integer(value, number_of_parts)

    assert len(result) == number_of_parts
    assert sum(result) == value
    assert result == sorted(result)
    if result:
        assert max(result) - min(result) <= 1
