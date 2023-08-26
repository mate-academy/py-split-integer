from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(10, 3)
    assert len(result) == 3
    assert max(result) - min(result) <= 1
    assert sum(result) == 10


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 40
    number_of_parts = 8
    waited_result = [5, 5, 5, 5, 5, 5, 5, 5]
    result = split_integer(value, number_of_parts)

    assert len(result) == number_of_parts
    assert max(result) - min(result) <= 1
    assert result == waited_result
    assert sum(result) == value


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 20
    number_of_parts = 1
    waited_result = [20]
    result = split_integer(value, number_of_parts)

    assert len(result) == number_of_parts
    assert max(result) - min(result) <= 1
    assert result == waited_result
    assert sum(result) == value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 7
    number_of_parts = 3
    waited_result = [2, 2, 3]
    result = split_integer(value, number_of_parts)

    assert len(result) == number_of_parts
    assert max(result) - min(result) <= 1
    assert result == waited_result
    assert sum(result) == value


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 3
    number_of_parts = 5
    waited_result = [0, 0, 1, 1, 1]
    result = split_integer(value, number_of_parts)

    assert len(result) == number_of_parts
    assert max(result) - min(result) <= 1
    assert result == waited_result
    assert sum(result) == value
