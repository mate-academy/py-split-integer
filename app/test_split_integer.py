import pytest


from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (80, 2),
        (2, 2),
        (102, 4)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int
) -> None:
    assert sum(split_integer(value, number_of_parts)) == value


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (80, 2, [40, 40]),
        (2, 2, [1, 1]),
        (120, 6, [20, 20, 20, 20, 20, 20])
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        number_of_parts: int,
        result: list
) -> None:
    assert split_integer(value, number_of_parts) == result


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (80, 1),
        (2, 1),
        (120, 1)
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int,
        number_of_parts: int
) -> None:
    assert split_integer(value, number_of_parts) == value


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (17, 4),
        (32, 6),
        (204, 8)
    ]
)
def test_difference_between_max_and_min_parts_should_not_exceed_one(
        value: int,
        number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)

    assert max(result) - min(result) <= 1


@pytest.mark.parametrize(
    "value,number_of_parts,sorted_result",
    [
        (204, 8, sorted([25, 25, 25, 25, 26, 26, 26, 26]))
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int,
        sorted_result: list
) -> None:
    assert split_integer(value, number_of_parts) == sorted_result


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (2, 4, [0, 0, 1, 1]),
        (3, 5, [0, 0, 1, 1, 1]),
        (1, 3, [0, 0, 1])
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_parts: int,
        result: list
) -> None:
    assert split_integer(value, number_of_parts) == result
