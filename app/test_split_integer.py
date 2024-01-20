from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(16, 3)) == 16, (
        "Error...sum of the parts should be equal to value")


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3], (
        "Error...should be equal parts when value divisible by parts")


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(26, 1) == [26]
    ), "Error...value should be one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    res = split_integer(35, 4)
    assert (
        res == sorted(res)
    ), "Error...should be sorted"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(5, 10) == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    ), "Error...should be zeros when value is less than number_of_parts"
