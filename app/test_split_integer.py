from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    parts = split_integer(17, 4)
    assert sum(parts) == 17, \
        "The sum of the parts should be equal to the original value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts = split_integer(6, 2)
    assert parts == [3, 3], \
        ("The value should be split into equal parts "
         "when divisible by number_of_parts")


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    parts = split_integer(8, 1)
    assert parts == [8], \
        "The part should equal the value when split into one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts = split_integer(17, 4)
    assert parts == sorted(parts), \
        "The parts should be sorted in ascending order"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    parts = split_integer(3, 5)
    assert parts == [0, 0, 1, 1, 1], \
        "Zeros should be added when value is less than number_of_parts"
