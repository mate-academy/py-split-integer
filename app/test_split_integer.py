import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, expected_result",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (5, 5, [1, 1, 1, 1, 1]),
        (3, 5, [0, 0, 1, 1, 1]),
        (20, 5, [4, 4, 4, 4, 4]),
        (100, 7, [14, 14, 14, 14, 14, 15, 15]),
    ],
)

def test_split_integer_examples_equal_expected(value: int,
                                               number_of_parts: int,
                                               expected_result: list
                                               ) -> None:
    assert split_integer(value, number_of_parts) == expected_result


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (5, 5),
        (3, 5),
        (20, 5),
        (100, 7),
    ],
)

def test_split_integer_properties_sorted_and_balanced(value: int, number_of_parts: int) -> None:
    result = split_integer(value, number_of_parts)

    assert len(result) == number_of_parts
    assert sum(result) == value

    assert all(isinstance(item, int) for item in result)

    assert result == sorted(result)

    assert max(result) - min(result) <= 1
