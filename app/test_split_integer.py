from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 6
    numbers_of_parts = 2
    parts = split_integer(value, numbers_of_parts)
    assert (sum(parts) == value), "Sum of the parts should be equal to_value."


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    numbers_of_parts = 2
    parts = split_integer(value, numbers_of_parts)
    assert (parts == [3, 3]), \
        "Should split into equal parts when value divisible by parts."


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    numbers_of_parts = 1
    parts = split_integer(value, numbers_of_parts)
    assert (len(parts) == numbers_of_parts), \
        "Should return part equals to value when split into one part."


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    numbers_of_parts = 4
    parts = split_integer(value, numbers_of_parts)
    assert (parts == [4, 4, 4, 5]), \
        "Parts should be sorted when they are not equal."


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    numbers_of_parts = 3
    parts = split_integer(value, numbers_of_parts)
    assert (parts == [0, 1, 1]), \
        "Should add zeros when value is less than number of parts."
