import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        pytest.param(12, 4, id="odd"),
        pytest.param(13, 4, id="even"),
        pytest.param(0, 1, id="zero")
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int) -> None:

    assert sum(split_integer(value, number_of_parts)) == value


@pytest.mark.parametrize(
    "value,number_of_parts,equal_part",
    [
        pytest.param(12, 4, 3, id="odd"),
        pytest.param(9, 3, 3, id="even"),
        pytest.param(0, 2, 0, id="zero"),
        pytest.param(1, 1, 1, id="single value")
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        number_of_parts: int,
        equal_part: int) -> None:

    assert all(num == equal_part
               for num in split_integer(value, number_of_parts))


@pytest.mark.parametrize(
    "value",
    [
        pytest.param(12, id="odd"),
        pytest.param(13, id="even"),
        pytest.param(0, id="zero")
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int) -> None:

    assert sum(split_integer(value, 1)) == value


@pytest.mark.parametrize(
    "value, number_of_parts,expected",
    [
        pytest.param(12, 5, [2, 2, 2, 3, 3], id="even"),
        pytest.param(13, 3, [4, 4, 5], id="odd"),
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int,
        expected: list) -> None:

    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize(
    "value,number_of_parts,expected",
    [
        pytest.param(1, 3, [0, 0, 1], id="odd"),
        pytest.param(2, 4, [0, 0, 1, 1], id="even"),
        pytest.param(1, 5, [0, 0, 0, 0, 1], id="additional")
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_parts: int,
        expected: list) -> None:

    assert split_integer(value, number_of_parts) == expected
