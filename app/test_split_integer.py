from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(32, 6)) == 32
    ), "Sum of the split parts should be equal to initial value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        len(set(split_integer(36, 6))) == 1
    ), "Split parts should be equal when value divisible by parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(32, 1)[0] == 32
    ), "Split part should be equal to initial value if parts == 1"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    ), "Should return sorted list if split parts not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(2, 6) == [0, 0, 0, 0, 1, 1]
    ), "Should add zeros if initial value < parts"
