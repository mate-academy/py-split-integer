import pytest

from app import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        pytest.param(8, 1, id="one part"),
        pytest.param(6, 2, id="divisible by parts"),
        pytest.param(17, 4, id="not divisible by parts"),
        pytest.param(32, 6, id="not divisible, more parts"),
        pytest.param(1, 5, id="value less than number of parts"),
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int
) -> None:
    result = split_integer.split_integer(value, number_of_parts)
    assert sum(result) == value
    assert len(result) == number_of_parts


@pytest.mark.parametrize(
    "value,number_of_parts,expected",
    [
        pytest.param(6, 2, [3, 3], id="6 into 2 parts"),
        pytest.param(12, 3, [4, 4, 4], id="12 into 3 parts"),
        pytest.param(10, 5, [2, 2, 2, 2, 2], id="10 into 5 parts"),
        pytest.param(5, 5, [1, 1, 1, 1, 1], id="5 into 5 parts"),
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        number_of_parts: int,
        expected: list[int]
) -> None:
    assert split_integer.split_integer(value, number_of_parts) == expected


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer.split_integer(8, 1) == [8]


@pytest.mark.parametrize(
    "value,number_of_parts,expected",
    [
        pytest.param(17, 4, [4, 4, 4, 5], id="17 into 4 parts"),
        pytest.param(32, 6, [5, 5, 5, 5, 6, 6], id="32 into 6 parts"),
        pytest.param(7, 3, [2, 2, 3], id="7 into 3 parts"),
        pytest.param(11, 3, [3, 4, 4], id="11 into 3 parts"),
        pytest.param(13, 5, [2, 2, 3, 3, 3], id="13 into 5 parts"),
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int,
        expected: list[int]
) -> None:
    result = split_integer.split_integer(value, number_of_parts)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    assert result == expected


@pytest.mark.parametrize(
    "value,number_of_parts,expected",
    [
        pytest.param(1, 2, [0, 1], id="1 into 2 parts"),
        pytest.param(3, 5, [0, 0, 1, 1, 1], id="3 into 5 parts"),
        pytest.param(1, 5, [0, 0, 0, 0, 1], id="1 into 5 parts"),
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_parts: int,
        expected: list[int]
) -> None:
    assert split_integer.split_integer(value, number_of_parts) == expected
