from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5], \
        "sum of 'parts' list not equal input value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (split_integer(6, 2) == [3, 3]), \
        "parts not equal when value divisible by parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (split_integer(8, 1) == [8]), \
        "Need to return value, when split into one part!"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (split_integer(32, 6) == [5, 5, 5, 5, 6, 6]), \
        "result list should be sorted!"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (split_integer(2, 5) == [0, 0, 0, 1, 1]), \
        "Should add zeros when value is less than parts!"
