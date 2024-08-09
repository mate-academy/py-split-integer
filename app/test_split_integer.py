from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(100, 7)) == 100
    ), "sum of parts must be equal to value"


def test_split_into_equal_parts_if_divisible_without_remainder() -> None:
    assert (
        split_integer(10, 5) == [2, 2, 2, 2, 2]
    ), "should split into equal parts when divisible has no remainder"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(95, 1) == [95]
    ), "should return value when number_of_parts is 1"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(76, 55) == sorted(split_integer(76, 55))
    ), "result must be sorted by asc"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        (split_integer(5, 10)) == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    ), "result must include zero when parts greater than value"
