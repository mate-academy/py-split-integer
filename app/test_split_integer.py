import pytest


from app.split_integer import split_integer


@pytest.mark.parametrize("value,number_of_parts", [(2, 1), (8, 2), (8, 3)])
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int, number_of_parts: int
) -> None:
    assert (
        sum(split_integer(value=value,
                          number_of_parts=number_of_parts)) == value
    ), f"Sum of parts should be equal to original value = {value}"


@pytest.mark.parametrize("value,number_of_parts", [(8, 1), (10, 5), (100, 4)])
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int, number_of_parts: int
) -> None:
    assert len(
        set(split_integer(value=value, number_of_parts=number_of_parts))
    ) == 1, (
        f"Split integer from value = {value} and number",
        f" of parts = {number_of_parts} should divide in equal parts",
    )


@pytest.mark.parametrize("value", [(13), (101)])
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int,
) -> None:
    assert split_integer(value=value, number_of_parts=1) == [value], (
        f"Split integer from value = {value} when"
        f" divided by 1 should split into one part"
    )


@pytest.mark.parametrize("value,number_of_parts", [(17, 4), (49, 8)])
def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int, number_of_parts: int
) -> None:

    list_of_neg_diff = [
        next_elem - prev_elem
        for prev_elem, next_elem in zip(
            split_integer(value, number_of_parts)[:-1],
            split_integer(value, number_of_parts)[1:],
        )
        if next_elem - prev_elem < 0
    ]

    assert not list_of_neg_diff, (
        f"Split_integer result from value = {value} and number"
        f" of parts = {number_of_parts} should be ordered"
    )


@pytest.mark.parametrize("value,number_of_parts", [(8, 9), (4, 8)])
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value: int, number_of_parts: int
) -> None:
    assert 0 in split_integer(
        value=value, number_of_parts=number_of_parts
    ), "Function should add zero when value is less than number of parts"
