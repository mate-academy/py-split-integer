from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    split_integer_result = split_integer(17, 4)
    assert sum(split_integer_result) == 17


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    split_integer_result = split_integer(8, 4)
    assert len(set(split_integer_result)) == 1


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    split_integer_result = split_integer(8, 1)
    assert split_integer_result == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    split_integer_result = split_integer(17, 4)
    assert split_integer_result == sorted(split_integer_result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    split_integer_result = split_integer(3, 5)
    assert split_integer_result == [0, 0, 1, 1, 1]
