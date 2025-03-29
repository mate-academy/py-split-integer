import pytest

from app.split_integer import split_integer

@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6])
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int,
        result: list
) -> None:
    assert sum(split_integer(value, number_of_parts)) == value


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6])
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        number_of_parts: int,
        result: list
) -> None:
    split = split_integer(value, number_of_parts)
    assert len(split) == number_of_parts, f"Expected {number_of_parts} parts, but got {len(split)}"
    assert all(part == split[0] for part in split), f"Expected equal parts, but got {split}"


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (8, 1, [8]),
        (6, 1, [3, 3]),
        (17, 1, [4, 4, 4, 5]),
        (32, 1, [5, 5, 5, 5, 6, 6])
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int,
        number_of_parts: int,
        result: list
) -> None:
    split = split_integer(value, number_of_parts)
    assert split == [value], f"Expected [{value}], but got {split}"


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6])
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int,
        result: list
) -> None:
    split = split_integer(value, number_of_parts)
    assert split == sorted(split), f"Expected sorted parts, but got {split}"


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6])
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_parts: int,
        result: list
) -> None:
    split = split_integer(value, number_of_parts)
    assert len(split) == number_of_parts, f"Expected {number_of_parts} parts, but got {len(split)}"
    expected_zeros = max(0, number_of_parts - value)
    assert split.count(0) == expected_zeros, f"Expected {expected_zeros} zeros, but got {split.count(0)}"
