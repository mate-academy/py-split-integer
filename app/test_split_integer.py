from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(
        split_integer(
            10, 6)) == 10,\
        "Sum of the parts should be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(12, 2) == [6, 6],\
        "Parts should be equal when value is divisible by parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(4, 1) == [4],\
        "When 'number_of_parts' = 1, part should be equal to value"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert sorted(split_integer(10, 3)) == [3, 3, 4]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 3) == [0, 1, 1]
