from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (sum(split_integer(50, 5)) == 50
            ), "sum of your elements should equal 50"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (split_integer(50, 5) == [10, 10, 10, 10, 10]
            ), "split 50 by 5 should equal [10, 10, 10, 10, 10]"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (split_integer(10, 1) == [10]
            ), "only one iteration, to split value"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
            ), "your list should be sorted"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (split_integer(3, 5) == [0, 0, 1, 1, 1]
            ), "when value is less than parts, should add zeros"
