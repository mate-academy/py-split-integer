import pytest
from app.split_integer import split_integer

@pytest.mark.parametrize(
    "value,number_of_parts,expected_result",
    [
        [10, 3, [3, 3, 4]],
        [28, 9, [3, 3, 3, 3, 3, 3, 3, 3, 4]]
        
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(value: int, number_of_parts: int, expected_result: list) -> None:
    act_result = split_integer(value, number_of_parts)
    assert act_result == expected_result


@pytest.mark.parametrize(
    "value,number_of_parts,expected_result",
    [
        [10, 5, [2, 2, 2, 2, 2]],
        [28, 9, [3, 3, 3, 3, 3, 3, 3, 3, 4]]
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(value: int, number_of_parts: int, expected_result: list) -> None:
    act_result = split_integer(value, number_of_parts)
    assert act_result == expected_result

@pytest.mark.parametrize(
    "value,number_of_parts,expected_result",
    [
        [10, 1, [10]],
        [15, 1, [15]]
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(value: int, number_of_parts: int, expected_result: list) -> None:
    act_result = split_integer(value, number_of_parts)
    assert act_result == expected_result


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    act_result = split_integer(10, 3)
    assert act_result == sorted(act_result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    act_result = split_integer(3, 5)
    assert act_result == [0, 0, 1, 1, 1]
