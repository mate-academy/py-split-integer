import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize("value,parts", [
    (8, 1),
    (45, 4),
    (100, 5),
    (6, 2),
    (17, 4),
    (32, 6)
])
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        parts: int,
) -> None:
    assert sum(split_integer(value, parts)) == value


@pytest.mark.parametrize("value,parts", [
    (15, 4),
    (131, 12),
    (10, 9)
])
def test_length_of_result_must_be_equal_parts(
        value: int,
        parts: int,
) -> None:
    assert len(split_integer(value, parts)) == parts


@pytest.mark.parametrize("value,parts", [
    (12, 4),
    (121, 11),
    (55, 5)
])
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int,
    parts: int
) -> None:
    assert split_integer(value, parts) == [value // parts] * parts


@pytest.mark.parametrize("value", [
    100, 1, 10
])
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int,
) -> None:
    assert split_integer(value, 1) == [value]


@pytest.mark.parametrize("value,parts", [
    (100, 12),
    (45, 10),
    (10, 4)
])
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        parts: int
) -> None:
    assert split_integer(value, parts) == sorted(split_integer(value, parts))


@pytest.mark.parametrize("value,parts", [
    (4, 5),
    (1, 10),
    (12, 24)
])
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        parts: int
) -> None:
    assert split_integer(value, parts).count(0) == parts - value


@pytest.mark.parametrize("value,parts", [
    (15, 4),
    (131, 12),
    (10, 9)
])
def test_split_integer_parts_diff_not_more_than_one(
        value: int,
        parts: int
) -> None:
    parts_list = split_integer(value, parts)
    assert max(parts_list) - min(parts_list) <= 1
