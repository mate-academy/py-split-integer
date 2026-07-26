from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value(
        value: int = 17,
        parts: int = 4) -> None:
    result = split_integer(value, parts)

    assert sum(result) == value and len(result) == parts


def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int = 6,
        parts: int = 2) -> None:
    assert split_integer(value, parts) == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int = 8,
        parts: int = 1) -> None:
    assert split_integer(value, parts) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int = 32,
        parts: int = 6) -> None:
    result = split_integer(value, parts)

    assert result == sorted(result) and max(result) - min(result) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int = 3,
        parts: int = 5) -> None:
    result = split_integer(value, parts)

    assert (
        len(result) == parts
        and sum(result) == value
        and result == [0, 0, 1, 1, 1]
    )
