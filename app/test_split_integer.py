from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(10, 5)) == 10, \
        "Sum of [2, 2, 2, 2, 2] should be equal to 10"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    for i in split_integer(10, 5):
        assert i == 2, "All parts should be same when value divisible by parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(10, 1) == [10], \
        "Part should be equal to value when split into one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6], \
        "List should be sorted when items not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(1, 2) == [0, 1], \
        "should add '0' when value < number of parts"
