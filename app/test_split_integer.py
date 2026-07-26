from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(20,5)) == 20
    ), "sum of all 5 parts should be equal to 20"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        len(set(split_integer(16, 4))) == 1
    ), "all parts should be equal if value divisible by parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(12, 1)
    assert (
        len(result) == 1 and result[0] == 12
    ), "result should be just one item in list and should be equal to value"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(33, 5)
    sorted_result = sorted(result)
    assert (
        result == sorted_result
    ), "list should be sorted"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(3, 6) == [0, 0, 0, 1, 1, 1]
    ), "if value is less than number_of_parts should add zeros"