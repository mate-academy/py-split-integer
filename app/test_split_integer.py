import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "first_number, second_number, expected_result",
    [
        pytest.param(
            8, 1, 8,
            id="sum_of_the_parts_should_be_equal_to_8"
        ),
        pytest.param(
            6, 2, 6,
            id="sum_of_the_parts_should_be_equal_to_6"
        ),
        pytest.param(
            17, 4, 17,
            id="sum_of_the_parts_should_be_equal_to_17"
        )
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        first_number: int,
        second_number: int,
        expected_result: int
) -> None:
    assert sum(split_integer(first_number, second_number)) == expected_result


@pytest.mark.parametrize(
    "first_number, second_number, expected_result",
    [
        pytest.param(
            8, 1, 1,
            id="amount_of_the_parts_should_be_equal_to_1"
        ),
        pytest.param(
            6, 2, 2,
            id="amount_of_the_parts_should_be_equal_to_2"
        ),
        pytest.param(
            17, 4, 4,
            id="amount_of_the_parts_should_be_equal_to_4"
        )
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        first_number: int,
        second_number: int,
        expected_result: int
) -> None:
    assert len(split_integer(first_number, second_number)) == expected_result


@pytest.mark.parametrize(
    "first_number, second_number, expected_result",
    [
        pytest.param(
            8, 1, 8,
            id="value_in_the_list_should_be_equal_to_8"
        ),
        pytest.param(
            6, 1, 6,
            id="value_in_the_list_should_be_equal_to_6"
        ),
        pytest.param(
            17, 1, 17,
            id="value_in_the_list_should_be_equal_to_17"
        )
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        first_number: int,
        second_number: int,
        expected_result: int
) -> None:
    assert split_integer(first_number, second_number) == [expected_result]


@pytest.mark.parametrize(
    "first_number, second_number, expected_result",
    [
        pytest.param(
            32, 6, [5, 5, 5, 5, 6, 6],
            id="list_should_be_sorted_when_they_are_not_equal"
        ),
        pytest.param(
            17, 4, [4, 4, 4, 5],
            id="list_should_be_sorted_when_they_are_not_equal"
        ),
        pytest.param(
            12, 2, [6, 6],
            id="list_should_be_sorted_when_they_are_not_equal"
        ),
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        first_number: int,
        second_number: int,
        expected_result: list
) -> None:
    assert split_integer(first_number, second_number) == expected_result


@pytest.mark.parametrize(
    "first_number, second_number, expected_result",
    [
        pytest.param(
            4, 6, [0, 0, 1, 1, 1, 1],
            id="result_should_add_zeros_when_"
            "value_is_less_than_number_of_parts"
        ),
        pytest.param(
            2, 8, [0, 0, 0, 0, 0, 0, 1, 1],
            id="result_should_add_zeros_when_"
            "value_is_less_than_number_of_parts"
        )
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        first_number: int,
        second_number: int,
        expected_result: list
) -> None:
    assert split_integer(first_number, second_number) == expected_result
    
