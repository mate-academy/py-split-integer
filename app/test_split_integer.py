from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(100, 3)) == 100, \
        f"Sum of parts: {sum(split_integer(100, 3))}, should be equal to 100"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(100, 2) == [50, 50], \
        f"The difference between the {max(split_integer(100, 2))} and " \
        f"{min(split_integer(100, 2))} number in the array should be <= 1"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(100, 1) == [100], \
        f"{split_integer(100, 1)} should be equal to "\
        f"[100] if number of parts is 1"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(100, 3) == [33, 33, 34], \
        "Result list should be sorted"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 4) == [0, 1, 1, 1], \
        "Function should add zeros when value is less than number of parts"
