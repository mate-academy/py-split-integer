import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    ("value", "number_of_parts", "expected"),
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
    ],
)
def test_split_integer_returns_expected_parts_for_known_examples(
    value: int, number_of_parts: int, expected: list[int]
) -> None:
    assert split_integer(value, number_of_parts) == expected


def test_result_should_contain_the_requested_number_of_parts() -> None:
    result = split_integer(17, 4)

    assert len(result) == 4


def test_parts_should_be_sorted_and_have_difference_at_most_one() -> None:
    result = split_integer(32, 6)

    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 5) == [0, 0, 0, 1, 1]
