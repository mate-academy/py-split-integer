from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value, number_of_parts = 8, 2
    assert sum(split_integer(value, number_of_parts)) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value, number_of_parts = 16, 4
    assert len(set(split_integer(value, number_of_parts))) == 1


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value, number_of_parts = 10, 1
    factual_result = split_integer(value, number_of_parts)
    assert len(factual_result) == 1 and factual_result[0] == value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value, number_of_parts = 17, 4
    factual_result = split_integer(value, number_of_parts)
    assert factual_result == sorted(factual_result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value, number_of_parts = 5, 8
    factual_result = split_integer(value, number_of_parts)
    assert factual_result.count(0) == number_of_parts - value
