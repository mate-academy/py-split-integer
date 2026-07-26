import pytest
from app.split_integer import split_integer


test_cases = [
    (8, 1),
    (6, 2),
    (17, 4),
    (32, 6),
    (12, 4),
    (10, 3),
    (3, 5),
    (5, 5),
]


@pytest.mark.parametrize("value, number_of_parts", test_cases)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int, number_of_parts: int
) -> None:
    assert sum(split_integer(value, number_of_parts)) == value


@pytest.mark.parametrize("value, number_of_parts", test_cases)
def test_should_return_integers_only(value: int, number_of_parts: int) -> None:
    assert all(isinstance(x, int) for x in split_integer(value, number_of_parts))


@pytest.mark.parametrize("value, number_of_parts", test_cases)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int, number_of_parts: int
) -> None:
    if value % number_of_parts == 0:
        expected = [value // number_of_parts] * number_of_parts
        assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize("value, number_of_parts", test_cases)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int, number_of_parts: int
) -> None:
    if number_of_parts == 1:
        assert split_integer(value, number_of_parts) == [value]


@pytest.mark.parametrize("value, number_of_parts", test_cases)
def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int, number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert result == sorted(result)


@pytest.mark.parametrize("value, number_of_parts", test_cases)
def test_difference_between_max_and_min_should_be_at_most_one(
    value: int, number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert max(result) - min(result) <= 1
