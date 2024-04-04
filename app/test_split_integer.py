import pytest


from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (2, 1, split_integer(2, 1)),
        (8, 2, split_integer(8, 2))
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(value: int,
                                                   number_of_parts: int,
                                                   result: list[int]) -> None:
    assert (
        split_integer(value=value, number_of_parts=number_of_parts) == result
    ), (f"Split_integer of value={value} and number",
        f" of parts = {number_of_parts} should be equal to {result}")


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (10, 5),
        (100, 4),
        (100, 3)
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int,
    number_of_parts: int
) -> None:
    assert (
        len(
            set(split_integer(value=value,
                              number_of_parts=number_of_parts
                              )
                )
        ) == 1
    ), (f"Split integer from value = {value} and number",
        f" of parts = {number_of_parts} should divide in equal parts")


@pytest.mark.parametrize(
    "value",
    [
        (13),
        (101),
        ("a")
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int
) -> None:
    assert (
        split_integer(value=value, number_of_parts=1) == [value]
    ), (f"Split integer from value = {value} when"
        f" divided by 1 should split into one part")


@pytest.mark.parametrize(
    "value,number_of_parts,result",
    [
        (17, 4, split_integer(17, 4)),
        (49, 8, split_integer(49, 8))
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(value: int,
                                                        number_of_parts: int,
                                                        result: list[int]
                                                        ) -> None:
    assert (
        split_integer(value=value, number_of_parts=number_of_parts) == result
    ), (f"Split integer from value = {value} and number"
        f" of parts = {number_of_parts} should be ordered")


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 9),
        (4, 8)
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value: int,
    number_of_parts: int
) -> None:
    assert (
        0 in split_integer(value=value, number_of_parts=number_of_parts)
    ), "Function should add zero when value is less than number of parts"
