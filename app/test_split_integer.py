from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(10, 5)) == 10, "Sum should be equal to 10"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(10, 5) == [2, 2, 2, 2, 2], \
        "Should be equal to [2, 2, 2, 2, 2]"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(10, 1) == [10], "Should be equal to [10]"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(12, 5) == [2, 2, 2, 3, 3]
        and max(split_integer(12, 5))
        - min(split_integer(12, 5)) in (0, 1)), \
        "Should be equal to [2, 2, 2, 3, 3] and difference between 1 and 0"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert len(set(split_integer(2, 5))) == 2, "Should be equal to 2"
