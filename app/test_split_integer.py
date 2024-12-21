import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, expected_sum", [(17, 4, 17), (8, 2, 8), (0, 3, 0)]
)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int, number_of_parts: int, expected_sum: int
) -> None:
    assert sum(split_integer(value, number_of_parts)) == expected_sum


@pytest.mark.parametrize(
    "value, number_of_parts, expected_result",
    [(12, 4, [3, 3, 3, 3]), (20, 5, [4, 4, 4, 4, 4])],
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int, number_of_parts: int, expected_result: list[int]
) -> None:
    assert split_integer(value, number_of_parts) == expected_result


@pytest.mark.parametrize(
    "value, number_of_parts, expected_result", [(8, 1, [8]), (50, 1, [50])]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int, number_of_parts: int, expected_result: list[int]
) -> None:
    assert split_integer(value, number_of_parts) == expected_result


@pytest.mark.parametrize("value, number_of_parts", [(17, 4), (23, 6), (19, 3)])
def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int, number_of_parts: int
) -> None:
    parts = split_integer(value, number_of_parts)
    assert parts == sorted(parts)


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (1, 2),
        (1, 10),
        (8, 9),
        (20, 25),
        (100, 102)
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value: int,
    number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert (
        len(result) == number_of_parts
        and result.count(0) == number_of_parts - value
    )
