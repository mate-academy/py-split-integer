from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(5, 5)) == 5
    ), "Sum of parts should be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(10, 5) == [2, 2, 2, 2, 2]
    ), "When value divisible by parts, all parts are equal"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(2, 1) == [2]
    ), "Should be one part equal to value when split into one"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(25, 8) == sorted(split_integer(25, 8))
    ), "Should be sorted"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(3, 7) == [0, 0, 0, 0, 1, 1, 1]
    ), "Should be zeros, when number of parts bigger then value"
