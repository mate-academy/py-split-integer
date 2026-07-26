import pytest


from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts,parts",
    [
        (6, 2, [3, 3]),
        (8, 1, [8]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (3, 5, [0, 0, 1, 1, 1])
    ]
)
def test_direct_examples_from_description(
        value: int,
        number_of_parts: int,
        parts: list
) -> None:
    assert split_integer(value=value, number_of_parts=number_of_parts) == parts
