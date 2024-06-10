from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    parts = split_integer(17, 4)
    assert sum(parts) == 17, "The sum of the parts should be equal to the original value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    divisible_parts = split_integer(30, 6)
    assert max(divisible_parts) - min(divisible_parts) == 0, "When divisible, parts should be exactly even"

    non_divisible_parts = split_integer(31,6)
    assert max(non_divisible_parts) - min(non_divisible_parts) <= 1, "When not divisible, difference between max and min parts should be no more than 1"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    parts = split_integer(8, 1)
    assert parts == [8], "The parts list should contain exactly the original value when split into one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts = split_integer(17, 4)
    assert all(parts[i] <= parts[i + 1] for i in range(len(parts) - 1)), "Parts should be sorted when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    parts = split_integer(4, 5)
    assert parts == [0, 1, 1, 1, 1], "Should distribute values with zero as needed when parts exceed the value"
