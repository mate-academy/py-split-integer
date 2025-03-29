import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        pytest.param(10, 2, 10, id="equally divisible number"),
        pytest.param(10, 3, 10, id="number divisible with remainder"),
        pytest.param(0, 3, 0, id="value is zero"),
        pytest.param(10, 0, 0, id="number of parts is zero"),
        pytest.param(0, 0, 0, id="value and number of parts are zero"),
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(value: int,
                                                   number_of_parts: int,
                                                   result: int) -> None:
    assert (sum(split_integer(value, number_of_parts)) == result
            ), f"Splitting {value} in {number_of_parts} should sum to {result}"


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        pytest.param(10, 2, [5, 5], id="equally divisible number"),
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        number_of_parts: int,
        result: list) -> None:
    assert (len(set(result)) == 1
            ), (f"Splitting {value} in {number_of_parts} "
                f"parts all values should be equal to {set(result)}")


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        pytest.param(10, 1, [10], id="split into one part"),
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int,
        number_of_parts: int,
        result: list) -> None:
    assert (result == split_integer(value, number_of_parts)
            ), (f"Splitting {value} in {number_of_parts} "
                f"parts should return a list with only one element: {result}")


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        pytest.param(10, 3, [3, 3, 4], id="number divisible with remainder"),
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(value: int,
                                                        number_of_parts: int,
                                                        result: list) -> None:
    assert (sorted(result) == split_integer(value, number_of_parts)
            ), (f"Splitting {value} in {number_of_parts} "
                f"parts should return a list sorted in "
                f"ascending order: {result}")


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        pytest.param(3, 5, [0, 0, 1, 1, 1],
                     id="split_parts is higher then the value"),
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_parts: int,
        result: list) -> None:
    assert (result == split_integer(value, number_of_parts)
            ), (f"Splitting {value} in {number_of_parts} "
                f"parts should return a list with only "
                f"zeros and ones: {result}")
