import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "initial_value,initial_parts,expected_sum",
    [
        (17, 4, 17),
        (32, 6, 32),
        (8, 1, 8,),
    ],
)
def test_correct_elements_sum(
        initial_value: int,
        initial_parts: int,
        expected_sum: int

) -> None:
    assert sum(split_integer(initial_value, initial_parts)) == expected_sum, \
        f"sum of the parts should be equal to {expected_sum}"


@pytest.mark.parametrize(
    "initial_value,initial_parts,expected_value",
    [
        (8, 1, 8),
    ],
)
def test_correct_result_if_split_into_one_part(
        initial_value: int,
        initial_parts: int,
        expected_value: int,
) -> None:
    assert split_integer(initial_value, initial_parts)[0] == expected_value, \
        "should return part equals to value when split into one part"


@pytest.mark.parametrize(
    "initial_value,initial_parts,expected_result",
    [
        (9, 3, 1),
        (17, 4, 2)
    ],
)
def test_equality_of_elements_in_list(
        initial_value: int,
        initial_parts: int,
        expected_result: int,
) -> None:
    assert (len(set(split_integer(initial_value, initial_parts)))
            == expected_result), \
        "test should split into equal parts when value divisible by parts"


@pytest.mark.parametrize(
    "initial_value,initial_parts,expected_result",
    [
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
    ]
)
def test_elements_are_sorted_ascending(
        initial_value: int,
        initial_parts: int,
        expected_result: list
) -> None:
    assert split_integer(initial_value, initial_parts) == expected_result, \
        "parts should be sorted when they are not equal"


@pytest.mark.parametrize(
    "initial_value,initial_parts,expected_result_list",
    [
        (2, 5, [0, 0, 0, 1, 1]),
        (3, 6, [0, 0, 0, 1, 1, 1]),
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        initial_value: int,
        initial_parts: int,
        expected_result_list: int,
) -> None:
    assert (split_integer(initial_value, initial_parts) == expected_result_list
            and len(split_integer(initial_value, initial_parts))
            == initial_parts), \
        "test should add zeros when value is less han number of parts"
