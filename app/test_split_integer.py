from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(10, 5)) == 10
    ), "Sum of the parts should be equal to value!"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(12, 3).count(12 / 3) == 3
    ), "Should split into equal parts when value divisible by parts!"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result_list = split_integer(2, 1)
    assert (
        len(result_list) == 1 and result_list[0] == 2
    ), "Should return part equals to value when split into one part!"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result_list = split_integer(13, 7)
    sorted_result_list = sorted(split_integer(13, 7))
    assert (
        result_list == sorted_result_list
    ), "Parts should be sorted when they are not equal!"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(2, 4) == [0, 0, 1, 1]
    ), "Should add zeros when value is less than number of parts!"
