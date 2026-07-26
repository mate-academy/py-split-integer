import pytest

from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(12, 4) == [3, 3, 3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(17, 1) == [17]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert sorted(split_integer(17, 4)) == split_integer(17, 4)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert sum(split_integer(10, 20)) == 10


def test_should_deference_between_part_less_one() -> None:
    result = split_integer(17, 4)
    min_, max_ = min(result), max(result)
    assert max_ - min_ <= 1


def test_count_result_equal_to_number_of_parts() -> None:
    assert len(split_integer(17, 4)) == 4


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        pytest.param(8, 1, [8], id="test1"),
        pytest.param(6, 2, [3, 3], id="test2"),
        pytest.param(17, 4, [4, 4, 4, 5], id="test3"),
        pytest.param(32, 6, [5, 5, 5, 5, 6, 6], id="test4")
    ]
)
def test_deference_data(value: int,
                        number_of_parts: int,
                        expected: list) -> None:
    assert split_integer(value, number_of_parts) == expected
