import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, result",
    [
        (12, 1, 12),
        (12, 2, 12),
        (-12, 5, -12),
        (12345, 2, 12345),
        (12345, 6, 12345),
        (12345, 100, 12345)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int,
        result: int
) -> None:
    output = sum(split_integer(value, number_of_parts))
    assert (output == result), \
        f"Sum of parts ({output}) not equal to value ({result})"


@pytest.mark.parametrize(
    "value, number_of_parts, result",
    [
        (12, 2, True),
        (12, 6, True),
        (-12340, 10, True),
        (12300, 100, True),
        (12, 5, False),
        (12340, 11, False),
        (-12300, 101, False)
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        number_of_parts: int,
        result: bool
) -> None:
    output = split_integer(value, number_of_parts)
    item_value = value / number_of_parts
    received = all(el == item_value for el in output)
    assert received == result, \
        "Should be split into equal parts"


@pytest.mark.parametrize(
    "value, number_of_parts, result",
    [
        (-123, 1, [-123]),
        (12, 1, [12]),
        (-12345, 1, [-12345]),
        (0, 1, [0])
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int,
        number_of_parts: int,
        result: list
) -> None:
    assert (split_integer(value, number_of_parts) == result), \
        f"Should return value: {value}"


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (3, 2),
        (15, 6),
        (12345, 2),
        (12345, 43),
        (-12345, 43),
        (12345, 100)
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int,
) -> None:
    output = split_integer(value, number_of_parts)
    assert output == sorted(output), \
        "Result should be sorted"


@pytest.mark.parametrize(
    "value, number_of_parts, result",
    [
        (-2, 5, [-1, -1, 0, 0, 0]),
        (0, 3, [0, 0, 0]),
        (7, 8, [0, 1, 1, 1, 1, 1, 1, 1]),
        (7, 15, [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1])
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_parts: int,
        result: int
) -> None:
    output = split_integer(value, number_of_parts)
    assert output == result, \
        "Should add zeros when value less then number_of_parts"
