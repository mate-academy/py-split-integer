from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(8, 3)) == 8
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(0, 5)) == 0


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(10, 5) == [2, 2, 2, 2, 2]
    assert split_integer(6, 3) == [2, 2, 2]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(0, 1) == [0]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts = split_integer(17, 4)
    assert parts == sorted(parts), "Parts are not sorted"
    assert max(parts) - min(parts) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(3, 5)
    assert result.count(0) == 2
    assert sum(result) == 3
    assert result == sorted(result)
