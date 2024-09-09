from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    initial_value = 32
    num_of_parts = 6
    result = split_integer(initial_value, num_of_parts)
    assert sum(result) == initial_value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    initial_value = 20
    num_of_parts = 4
    result = split_integer(initial_value, num_of_parts)
    assert len(set(result)) <= 1


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    initial_value = 3204
    num_of_parts = 1
    result = split_integer(initial_value, num_of_parts)
    assert result == [initial_value]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    initial_value = 32
    num_of_parts = 6
    result = split_integer(initial_value, num_of_parts)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    initial_value = 10
    num_of_parts = 24
    result = split_integer(initial_value, num_of_parts)
    assert result.count(0) == num_of_parts - initial_value
