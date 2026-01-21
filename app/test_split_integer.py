import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
    ],
    ids=[
        "single_part",
        "equal_parts",
        "parts_with_one_difference",
        "multiple_larger_parts"
    ]
)
def test_split_integer_examples(
    value: int,
    number_of_parts: int,
    expected: list[int]
) -> None:
    assert split_integer(value, number_of_parts) == expected


def test_split_integer_with_equal_parts() -> None:
    assert split_integer(10, 2) == [5, 5]


def test_split_integer_parts_should_be_sorted_ascending() -> None:
    assert split_integer(11, 3) == [3, 4, 4]


def test_split_integer_difference_is_at_most_one() -> None:
    # Aqui a variável é necessária para evitar duplicar o processamento
    result = split_integer(100, 9)
    assert max(result) - min(result) <= 1


def test_split_integer_total_sum_is_correct() -> None:
    assert sum(split_integer(35, 8)) == 35


def test_split_integer_number_of_parts_is_correct() -> None:
    assert len(split_integer(20, 5)) == 5
