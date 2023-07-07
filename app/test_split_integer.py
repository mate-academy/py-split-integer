from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(32, 6)
    assert sum(result) == 32


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(17, 4)
    assert len(result) == 4


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(8, 1)
    assert result[0] == 8


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(32, 6)
    assert result == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(2, 4)
    add__zero_result =  result[:2]
    assert add__zero_result == [0, 0]
