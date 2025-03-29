from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(8, 1)) == 8, (
        "Sum of the returned result should be equal to value!"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3], (
        "Should split value into equal parts if value divisible by parts!"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8], (
        "Should return result equals to value if `number_of_parts` is 1!"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6], (
        "Returned list should be sorted if elements are not equal!"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(1, 4) == [0, 0, 0, 1], (
        "Should add zeros if `value` is less than `number_of_parts`!"
    )
