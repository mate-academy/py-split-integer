from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(10, 3)) == 10, "The sum of the parts should be equal to the original value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(12, 4) == [3, 3, 3,
                                    3], "Should split into equal parts when value is divisible by number of parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(15, 1) == [
        15], "When splitting into one part, it should return the value as a single-element list"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(11, 3) == [3, 4,
                                    4], "Parts should be sorted, and the difference between max and min should be <= 1"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1], "Should add zeros when value is smaller than number of parts"