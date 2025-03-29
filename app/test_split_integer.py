from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(12, 3)) == 12), (
        "Sum of the parts should be equal to value"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(12, 3) == [4, 4, 4]), (
        "Value should split into equal parts if value divisible by parts"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(12, 1) == [12]), (
        "The result list should contain only 'value' if number of parts is 1"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(22, 4) == [5, 5, 6, 6]), (
        "Result list should be sorted from lower to higher if possible"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(4, 5) == [0, 1, 1, 1, 1]), (
        "Zeros should be added if value < number of parts"
    )
