import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (74, 10, 74),
        (37, 7, 37),
        (100, 1, 100),
    ],
    ids=[
        "sum of the parts should be equal to 74 when initiall value is 74",
        "sum of the parts should be equal to 37 when initiall value is 37",
        "sum of the parts should be equal to 100 when initiall value is 100",
    ],
)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int, number_of_parts: int, expected: int
) -> None:
    assert sum(split_integer(value, number_of_parts)) == expected


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (16, 4, [4, 4, 4, 4]),
        (30, 6, [5, 5, 5, 5, 5, 5]),
        (70, 10, [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]),
    ],
    ids=[
        "should split 16 into 4 equal parts",
        "should split 30 into 6 equal parts",
        "should split 70 into 10 equal parts",
    ],
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int, number_of_parts: int, expected: list[int]
) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (17, 1, [17]),
        (59, 1, [59]),
        (7, 1, [7]),
    ],
    ids=[
        "should return the same parts when splitting 17 into 1 part",
        "should return the same parts when splitting 59 into 1 part",
        "should return the same parts when splitting 7 into 1 part",
    ],
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int, number_of_parts: int, expected: list[int]
) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (33, 6, [5, 5, 5, 6, 6, 6]),
        (50, 9, [5, 5, 5, 5, 6, 6, 6, 6, 6]),
        (100, 3, [33, 33, 34]),
    ],
    ids=[
        "should split 33 into 6 parts with some parts being larger",
        "should split 50 into 9 parts with some parts being larger",
        "should split 100 into 3 parts with some parts being larger",
    ],
)
def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int, number_of_parts: int, expected: list[int]
) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (2, 3, [0, 1, 1]),
        (0, 1, [0]),
        (0, 3, [0, 0, 0]),
    ],
    ids=[
        "should split 2 into 3 parts with some parts being zeros",
        "should split 0 into 1 part",
        "should split 0 into 3 parts with all parts being zeros",
    ],
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value: int, number_of_parts: int, expected: list[int]
) -> None:
    assert split_integer(value, number_of_parts) == expected
