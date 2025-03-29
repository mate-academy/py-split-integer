from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(17, 3)) == 17
    ), "Sum of the parts have to be equal to value!!!"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(15, 3) == [5, 5, 5]
    ), "All parts have to be equal if value divisible by parts!!!"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(33, 1) == [33]
    ), "If you split value into one part value should be equal to result!!!"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(32, 6) == sorted(split_integer(32, 6))
    ), "Result have to be sorted!!!"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(3, 5) == [0, 0, 1, 1, 1]
    ), "If value is less than number of parts you have add zeros!!!"
