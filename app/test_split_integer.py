from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(10, 3)) == 10
    ), "Sum of the parts should be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        sum(split_integer(6, 3))
        % len(split_integer(6, 3)) == 0
    ), ("The sum of the numbers in the list must be divisible by the number"
        " of parts without a remainder ")


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(5, 1) == [5]
    ), "Should return part equals to value when split into one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(25, 8)
        == sorted(split_integer(25, 8))
    ), "Parts should be sorted when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(5, 11)
    assert (
        len(result) == 11
    ), "The number of parts must be correct"
    assert (
        sum(result) == 5
    ), "The sum of all parts must be equal to the original number"
    assert (
        result.count(0) == 6
    ), ("The number of zeros must be equal to the "
        "difference between the number of list parts and the value")
