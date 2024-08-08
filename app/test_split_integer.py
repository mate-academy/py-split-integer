from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (sum(split_integer(36, 6)) == 36), \
        "sum of elements in the result list should be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert set(split_integer(36, 6)) == {6}, \
        ("if value can be divided by number_of_parts equally, "
         "result list should contain the same numbers")


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(36, 1) == [36], \
        ("if you are splitting value into 1 part, "
         "result list should contain only this value")


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert sorted(split_integer(32, 6)) == split_integer(32, 6), \
        "if result list contains different numbers, they should be sorted"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 3) == [0, 1, 1], \
        ("if number of parts is bigger then the value, "
         "result list should contain zeros")
