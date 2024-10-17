from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(32, 6)) == 32, \
        "Sum of the parts should be equal to value."


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(4, 2) == [2, 2], \
        "Parts should be equal if value divisible by parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(7, 1) == [7], \
        "Parts should be equal to value if number of parts equal to 1"



def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5], \
        "Parts list should be sorted"



def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 3) == [0, 1, 1], \
        "Parts should contain zeros if value is less than number of parts"

