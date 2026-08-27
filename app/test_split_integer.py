from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(12, 3)) == 12
    ), "Sum must equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        max(split_integer(6, 2)) == min(split_integer(6, 2))
    ), "Parts should be equal"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(8, 1) == [8]
    ), "Splitting should return a list with original value"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(32, 6) == sorted(split_integer(32, 6))
    ), "Result list of parts must be sorted"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(3, 5) == [0, 0, 1, 1, 1]
    ), "Should add zeroes when value is less than number of parts"


def test_should_return_an_array_containing_exactly_number_of_parts() -> None:
    assert (
        len(split_integer(10, 3)) == 3
    ), "The length of result list must equal number of parts"


def test_the_difference_between_the_max_and_min_number_in_the_array() -> None:
    assert (
        max(split_integer(10, 3)) - min(split_integer(10, 3)) <= 1
    ), ("The difference between the maximum and"
        " minimum parts must not be more then 1")
