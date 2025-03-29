import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, result",
    [
        pytest.param(8, 3, 8, id="value 8"),
        pytest.param(12, 4, 12, id="value 12"),
        pytest.param(20, 5, 20, id="value 20")
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int,
        result: int) -> None:
    assert (sum(split_integer(value, number_of_parts)) == result), \
        (f"When valus is {value} and number_of_parts "
         f"is {number_of_parts}, the sum must be {result}")


@pytest.mark.parametrize(
    "value, number_of_parts, result_list",
    [
        pytest.param(8, 4, [2, 2, 2, 2],
                     id="value 8 and number of parts 4"),
        pytest.param(12, 3, [4, 4, 4],
                     id="value 12 and number of parts 3"),
        pytest.param(20, 5, [4, 4, 4, 4, 4],
                     id="value 20 and number of parts 5")
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        number_of_parts: int,
        result_list: list) -> None:
    assert (split_integer(value, number_of_parts) == result_list), \
        (f"When valus is {value} and number_of_parts is {number_of_parts}, "
         f"the result list must be {result_list}")


@pytest.mark.parametrize(
    "value, number_of_parts, result",
    [
        pytest.param(8, 1, [8], id="value 8"),
        pytest.param(12, 1, [12], id="value 12"),
        pytest.param(20, 1, [20], id="value 20")
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int,
        number_of_parts: int,
        result: list) -> None:
    assert split_integer(value, number_of_parts) == result, \
        (f"When valus is {value} and number_of_parts is {number_of_parts}, "
         f"the result must be {result}")


@pytest.mark.parametrize(
    "value, number_of_parts, sorted_result_list",
    [
        pytest.param(8, 3, sorted([2, 3, 3]), id="value 8"),
        pytest.param(12, 5, sorted([2, 2, 2, 3, 3]), id="value 12"),
        pytest.param(20, 4, sorted([5, 5, 5, 5]), id="value 20")
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int,
        sorted_result_list: list) -> None:
    assert split_integer(value, number_of_parts) == sorted_result_list, \
        (f"When valus is {value} and number_of_parts is {number_of_parts}, "
         f"the result list must be {sorted_result_list}")


@pytest.mark.parametrize(
    "value, number_of_parts, result",
    [
        pytest.param(8, 10,
                     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                     id="value 8"),
        pytest.param(12, 15,
                     [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     id="value 12"),
        pytest.param(20, 25,
                     [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], id="value 20")
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_parts: int,
        result: list) -> None:
    assert split_integer(value, number_of_parts) == result, \
        (f"When valus is {value} and number_of_parts is {number_of_parts}, "
         f"the result list must be {result}")
