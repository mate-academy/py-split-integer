from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 10
    number_of_parts = 3
    parts = split_integer(value, number_of_parts)
    assert sum(parts) == value,\
        "The sum of the parts should equal the original value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 8
    number_of_parts = 4
    parts = split_integer(value, number_of_parts)
    assert parts == [2, 2, 2, 2],\
        "Should split evenly into equal parts when divisible"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 5
    number_of_parts = 1
    parts = split_integer(value, number_of_parts)
    assert parts == [5],\
        "Should return the part equal to the value when split into one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 10
    number_of_parts = 3
    parts = split_integer(value, number_of_parts)
    assert parts == [3, 3, 4],\
        "Parts should be sorted in ascending order when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    number_of_parts = 5
    parts = split_integer(value, number_of_parts)
    assert parts == [0, 0, 0, 1, 1],\
        "Should add zeros when value is less than number of parts"
