from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(17, 5)
    assert sum(result) == 17
    assert len(result) == 5


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(25, 5)
    assert len(set(result)) == 1
    assert result[0] == 5
    assert len(result) == 5


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 25
    result = split_integer(value, 1)
    assert result[0] == value
    assert len(result) == 1


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    usual_func_result = split_integer(17, 5)
    sorted_func_result = sorted(split_integer(17, 5))
    assert usual_func_result == sorted_func_result


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(0, 5)
    assert sum(result) == 0
    assert all(x == 0 for x in result)
