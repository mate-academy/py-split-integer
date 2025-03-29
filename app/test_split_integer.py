from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    parts = split_integer(6, 2)
    assert (
        sum(parts) == 6
    ), ("Should return a list of parts whose sum is equal to the value.")


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts = split_integer(6, 2)
    assert (
        len(set(parts)) == 1
    ), ("Should return a list of equal parts when value divisible by parts.")


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(8, 1) == [8]
    ), (
        "Should return a list of one part equal to the value "
        "when split into one part"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(17, 4) == [4, 4, 4, 5]
    ), ("Should return a sorted list when parts are not equal")


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(2, 4) == [0, 0, 1, 1]
    ), (
        "Should return a list with zeros at "
        "the beginning when value is less "
        "than number of parts."
    )
