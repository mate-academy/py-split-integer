from app.split_integer import split_integer
import pytest


@pytest.mark.parametrize(
    "value,number_of_parts,expected_list",
    [
        (100, 3, [33, 33, 34]),
        (100, 2, [50, 50]),
        (100, 1, [100]),
        (3, 4, [0, 1, 1, 1]),
    ],
    ids=[f"Sum of parts: {sum(split_integer(100, 3))}, should be equal to 100",
         (f"The difference between the {max(split_integer(100, 2))} and "
          f"{min(split_integer(100, 2))} number in the array should be <= 1"),
         (f"{split_integer(100, 1)} should be equal to "
          f"[100] if number of parts is 1"),
         "Function should add zeros when value is less than number of parts",
         ]
)
def test_should_return_correct_value(
        value: int,
        number_of_parts: int,
        expected_list: list
) -> None:
    assert split_integer(value, number_of_parts) == expected_list
