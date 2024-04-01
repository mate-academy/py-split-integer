from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert 10 == sum(split_integer(10, 5))


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert 20 == sum(split_integer(20, 4))
    assert 4 == len(split_integer(20, 4))
    assert all(part == 20 // 4 for part in split_integer(20, 4))


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert 15 == sum(split_integer(15, 1))


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == sorted(split_integer(17, 4))


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(5, 8)
    assert len(result) == 8 and 0 in result
