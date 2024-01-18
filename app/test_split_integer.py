from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(10, 4)) == 10, \
        "Expected sum of the parts "\
        f"to be equal 10, but got {sum(split_integer(10, 4))}."


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3], \
        f"Expected equal parts, but got {split_integer(6, 2)}."


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(5, 1) == [5], \
        "Expected one part to be equal to 5, "\
        f"but got {split_integer(5, 1)}."


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(7, 2) == [3, 4], \
        "Expected two parts to be sorted, "\
        f"but got {split_integer(7, 2)}."


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 3) == [0, 1, 1], \
        "Expected zeros to be added "\
        "when value < number of parts."
