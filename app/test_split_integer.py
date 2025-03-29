import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, expected_sum",
    [
        pytest.param(
            17, 4, 17,
            id="checks sum of the parts is equal to value"
        )
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int,
    number_of_parts: int,
    expected_sum: int,
) -> None:
    result = split_integer(value, number_of_parts)
    assert sum(result) == expected_sum


@pytest.mark.parametrize(
    "value, number_of_parts, expected_result",
    [
        pytest.param(
            6, 2, [3, 3],
            id="Split into equal parts when value divisible by parts"
        )
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int,
    number_of_parts: int,
    expected_result: list[int],
) -> None:
    assert split_integer(value, number_of_parts) == expected_result


@pytest.mark.parametrize(
    "value, number_of_parts, expected_result",
    [
        pytest.param(
            8, 1, [8],
            id="Should return value as single element when split into one part"
        )
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int,
    number_of_parts: int,
    expected_result: list[int],
) -> None:
    assert split_integer(value, number_of_parts) == expected_result


@pytest.mark.parametrize(
    "value, number_of_parts, expected_result",
    [
        pytest.param(
            17, 4, [4, 4, 4, 5],
            id="Parts should be sorted when they are not equal"
        )
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int,
    number_of_parts: int,
    expected_result: list[int],
) -> None:
    result = split_integer(value, number_of_parts)
    assert result == expected_result
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


@pytest.mark.parametrize(
    "value, number_of_parts, expected_result",
    [
        pytest.param(
            2, 4, [0, 0, 1, 1],
            id="Should add zeros when value is less than number of parts"
        )
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value: int,
    number_of_parts: int,
    expected_result: list[int],
) -> None:
    assert split_integer(value, number_of_parts) == expected_result
