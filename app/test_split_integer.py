from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    parts = split_integer(value=8, number_of_parts=2)

    assert (
        parts[0] + parts[1] == 8
    ), "Sum of the parts should be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts = split_integer(value=12, number_of_parts=3)

    assert (
        parts[0] == parts[1] == parts[2]
    ), "Parts should be equal when value divisible by parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    parts = split_integer(value=15, number_of_parts=1)

    assert (
        parts == [15]
    ), "part should be equal to value when nuber_of_parts equals 1"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts = split_integer(value=32, number_of_parts=6)

    assert (
        parts == [5, 5, 5, 5, 6, 6]
    ), "Parts should be sorted when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    parts = split_integer(value=4, number_of_parts=5)

    assert (
        parts == [0, 1, 1, 1, 1]
    ), "Parts should add zeros when value is less than number_of_parts"
