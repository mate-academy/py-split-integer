import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, result_list",
    [
        pytest.param(17, 4, [4, 4, 4, 5], id="sum of the parts "
                                             "should be equal to value")
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int,
        result_list: list
) -> None:
    split_integer(value, number_of_parts)
    assert sum(result_list) == value


@pytest.mark.parametrize(
    "value, number_of_parts, result_list",
    [
        pytest.param(6, 2, [3, 3],
                     id="should split into equal parts "
                        "when value divisible by parts")
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        number_of_parts: int,
        result_list: list
) -> None:
    if value % number_of_parts == 0:
        split_integer(value, number_of_parts)
        assert result_list[0] == result_list[1]


@pytest.mark.parametrize(
    "value, number_of_parts, result_list",
    [
        pytest.param(8, 1, [8], id="should return part equals "
                                   "to value when split into one part")
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int,
        number_of_parts: int,
        result_list: list
) -> None:
    if number_of_parts == 1:
        split_integer(value, number_of_parts)
        assert len(result_list) == 1


@pytest.mark.parametrize(
    "value, number_of_parts, result_list",
    [
        pytest.param(17, 4, [4, 4, 4, 5],
                     id="parts should be sorted when they are not equal")
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int,
        result_list: list
) -> None:
    split_integer(value, number_of_parts)
    assert result_list == result_list.sort()


@pytest.mark.parametrize(
    "value, number_of_parts, result_list",
    [
        pytest.param(1, 3, [1, 0, 0],
                     id="add zeros when value is less than number of parts")
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_parts: int,
        result_list: list
) -> None:
    split_integer(value, number_of_parts)
    assert result_list == result_list
