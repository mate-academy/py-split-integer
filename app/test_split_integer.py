import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_pairs",
    [
        (1, 4), (545, 1), (56, 45), (56, 56), (4, 4), (3, 1)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_pairs: int
) -> None:
    assert sum(split_integer(value, number_of_pairs)) == value


@pytest.mark.parametrize(
    "value,number_of_pairs,expected_list",
    [
        (5, 5, [1, 1, 1, 1, 1]),
        (2, 2, [1, 1]),
        (20, 5, [4, 4, 4, 4, 4]),
        (20, 4, [5, 5, 5, 5]),
        (12, 2, [6, 6]),
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        number_of_pairs: int,
        expected_list: list
) -> None:
    assert split_integer(value, number_of_pairs) == expected_list


@pytest.mark.parametrize(
    "value,expected_result",
    [
        (1, [1]), (545, [545]), (56, [56]), (3, [3])
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int,
        expected_result: list
) -> None:
    assert split_integer(value, 1) == expected_result


@pytest.mark.parametrize(
    "value,number_of_pairs,expected_result",
    [
        (34, 5, [6, 7, 7, 7, 7]),
        (3, 2, [1, 2]),
        (21, 5, [4, 4, 4, 4, 5]),
        (23, 4, [5, 6, 6, 6]),
        (5, 2, [2, 3]),
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_pairs: int,
        expected_result: list
) -> None:
    assert split_integer(value, number_of_pairs) == expected_result


@pytest.mark.parametrize(
    "value,number_of_pairs,expected_result",
    [
        (4, 5, [0, 1, 1, 1, 1]),
        (2, 5, [0, 0, 0, 1, 1]),
        (3, 4, [0, 1, 1, 1]),
        (0, 7, [0, 0, 0, 0, 0, 0, 0]),
        (5, 7, [0, 0, 1, 1, 1, 1, 1]),
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_pairs: int,
        expected_result: list
) -> None:
    assert split_integer(value, number_of_pairs) == expected_result
