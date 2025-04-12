from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    number_of_parts = 4
    parts = split_integer(value, number_of_parts)
    assert sum(parts) == value, \
        f"Sum of the parts should be equal to {value}"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts = split_integer(16, 4)
    assert parts == [4, 4, 4, 4], \
        "All digits must be equal, if value divisible by parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    parts = split_integer(17, 1)
    assert parts == [17], \
        "Part must be equal value, when part equal one"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts = split_integer(18, 4)
    assert parts == sorted(parts), \
        "If division with remaining digits must be sorted"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    parts = split_integer(3, 5)
    assert parts == sorted(parts)
    assert sum(parts) == 3
    assert len(parts) == 5, \
        "If value < num_of_parts, all parts must be zero"
