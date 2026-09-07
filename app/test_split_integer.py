from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(8, 2)) == 8
    ), "Sum of the parts should be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        len(set(split_integer(8, 4))) == 1
    ), "Parts should be equal when value is divisible by parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(8, 1) == [8]
    ), "Result should be equal to value when is divided by one"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts = split_integer(8, 3)
    assert (
        parts == sorted(parts)
    ), "Part should be sorted if not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(4, 5) == [0, 1, 1, 1, 1]
    ), "Should add zeros when value is less than number of parts"
