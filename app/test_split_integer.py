import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize("value, number_of_parts", [(6, 2)])
def test_sum_of_the_parts_should_be_equal_to_value(value, number_of_parts) -> None:
    parts = split_integer(value, number_of_parts)
    assert sum(parts) == value


@pytest.mark.parametrize("value, number_of_parts", [(32, 6)])
def test_should_split_into_equal_parts_when_value_divisible_by_parts(value, number_of_parts) -> None:
    parts = split_integer(value, number_of_parts)
    assert len(parts) == number_of_parts


@pytest.mark.parametrize("value, number_of_parts", [(8, 1)])
def test_should_return_part_equals_to_value_when_split_into_one_part(value, number_of_parts) -> None:
    parts = split_integer(value, number_of_parts)
    if len(parts) == 1:
        assert parts[0] == value


@pytest.mark.parametrize("value, number_of_parts", [(17, 4)])
def test_parts_should_be_sorted_when_they_are_not_equal(
        value,
        number_of_parts
) -> None:
    parts = split_integer(value, number_of_parts)
    assert parts == sorted(parts)


# @pytest.mark.parametrize(
#     "value, number_of_parts, expected_res",
#     [
#         (8, 1, [8]),
#     ]
# )
# def test_should_add_zeros_when_value_is_less_than_number_of_parts(
#         value,
#         number_of_parts,
#         expected_res
# ) -> None:
#     split_integer(value, number_of_parts)
#     if number_of_parts is None:
#         assert number_of_parts == 0
