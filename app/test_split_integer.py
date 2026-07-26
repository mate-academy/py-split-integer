import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize("value, number_of_parts", [(8, 2)])
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int
) -> None:
    assert sum(split_integer(value, number_of_parts)) == value, \
        "Sum of the parts is not equal to value"


@pytest.mark.parametrize("value, number_of_parts", [(8, 2)])
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        number_of_parts: int
) -> None:
    assert len(set(split_integer(value, number_of_parts))) == 1, \
        "Value not divisible by number of parts"


@pytest.mark.parametrize("value, number_of_parts", [(8, 1)])
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int,
        number_of_parts: int
) -> None:
    assert split_integer(value, number_of_parts)[0] == value, \
        "One part not equal to value"


@pytest.mark.parametrize("value, number_of_parts", [(7, 2)])
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    for i in range(len(result) - 1):
        assert result[i] <= result[i + 1], "Parts not sorted"


@pytest.mark.parametrize("value, number_of_parts", [(1, 2)])
def test_parts_meet_constraints_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert len(result) == number_of_parts
    assert sum(result) == value
    assert result == sorted(result)

    max_part = max(result)
    min_part = min(result)
    assert max_part - min_part <= 1


def test_examples_from_description() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
