import pytest

from app.split_integer import split_integer


@pytest.fixture()
def input_equal_integers() -> dict:
    return {"value": 4, "number_of_parts": 4}


@pytest.fixture()
def value_less_than_number_case() -> dict:
    return {"value": 1, "number_of_parts": 3}


@pytest.fixture()
def uneven_split_case() -> dict:
    return {"value": 5, "number_of_parts": 3}


def test_sum_of_the_parts_should_be_equal_to_value(
        input_equal_integers: dict
) -> None:
    assert (sum(
        split_integer(
            input_equal_integers["value"],
            input_equal_integers["number_of_parts"])
    ) == input_equal_integers["value"])


def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        input_equal_integers: dict
) -> None:
    result = split_integer(
        input_equal_integers["value"],
        input_equal_integers["number_of_parts"]
    )
    assert all(part == result[0] for part in result)


def test_should_return_part_equals_to_value_when_split_into_one_part(
        input_equal_integers: dict
) -> None:
    result = split_integer(input_equal_integers["value"], 1)
    assert result == [input_equal_integers["value"]]


def test_parts_should_be_sorted_when_they_are_not_equal(
        uneven_split_case: dict
) -> None:
    result = split_integer(
        uneven_split_case["value"],
        uneven_split_case["number_of_parts"]
    )
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value_less_than_number_case: dict
) -> None:
    number_of_parts = value_less_than_number_case["number_of_parts"]
    value = value_less_than_number_case["value"]
    result = split_integer(
        value,
        number_of_parts
    )
    assert (len(result) == number_of_parts
            and sum(result[:number_of_parts - value]) == 0)


def test_should_distribute_remaining_value_evenly(
        uneven_split_case: dict
) -> None:
    result = split_integer(
        uneven_split_case["value"],
        uneven_split_case["number_of_parts"]
    )
    assert sum(result) == uneven_split_case["value"]
    assert max(result) - min(result) <= 1
