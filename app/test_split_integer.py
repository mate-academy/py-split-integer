import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, result",
    [
        pytest.param(
            6, 2, [3, 3], id="sum_of_the_parts_should_be_equal_to_value"
        ),
        pytest.param(
            16, 4, [4, 4, 4, 4],
            id="split_into_equal_parts_when_value_divisible_by_parts"
        ),
        pytest.param(
            6, 1, [6],
            id="return_part_equals_to_value_when_split_into_one_part"
        ),
        pytest.param(
            17, 3, [5, 6, 6],
            id="parts_should_be_sorted_when_they_are_not_equal"
        ),
        pytest.param(
            1, 2, [0, 1],
            id="add_zeros_when_value_is_less_than_number_of_parts"
        )
    ]
)
def test_split_integer(value: int, number_of_parts: int, result: list) -> None:
    assert (
        split_integer(value, number_of_parts) == result
    )
