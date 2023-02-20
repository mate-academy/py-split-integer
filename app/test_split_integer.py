from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    target = 500
    parts_number = 10
    result = split_integer(target, parts_number)
    assert sum(result) == target


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    target = 6
    parts_number = 2
    result = split_integer(target, parts_number)
    assert result == [target // parts_number] * parts_number


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    target = 7
    result = split_integer(target, 1)
    assert len(result) == 1 and result[0] == target


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    target = 32
    parts_number = 6
    result = split_integer(target, parts_number)
    assert target % parts_number != 0 and result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    target = 3
    parts_number = 5
    result = split_integer(target, parts_number)
    assert target < parts_number and parts_number - target == result.count(0)
