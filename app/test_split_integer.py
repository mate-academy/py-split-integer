from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17, \
        "Sum of the parts should be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2)[0] == split_integer(6, 2)[1], \
        "Function 'split_integer' should split value into equal parts when value divisible by parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8], \
        "The result list should contain one element equals to value when split into one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6], \
        "Result list should be sorted when its parts are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(0, 4) == [0, 0, 0, 0], \
        "Result should contain zeros when value is less then number of parts"
    assert split_integer(2, 7) == [0, 0, 0, 0, 0, 1, 1], \
        "Result should contain zeros when value is less then number of parts"
