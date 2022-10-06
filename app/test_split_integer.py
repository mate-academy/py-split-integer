import pytest


from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts,expected_result",
    [
        (17, 4, [4, 4, 4, 5]),
        (6, 2, [3, 3]),
        (8, 1, [8]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (4, 6, [0, 0, 1, 1, 1, 1])
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int,
        expected_result: list
) -> None:

    assert split_integer(value, number_of_parts) == expected_result
