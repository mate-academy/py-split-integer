from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(value=29, number_of_parts=8)) == 29
    ), "Sum of the parts should be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(value=20, number_of_parts=5) == [4, 4, 4, 4, 4]
    ), "Should split into equal parts when value divisible by parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(value=9, number_of_parts=1)[0] == 9
    ), "Should return part equal to value when split into one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(value=29, number_of_parts=10)
    # if sorted(result)[0] != sorted(result)[-1]:

    assert (
        split_integer(value=29, number_of_parts=10) == sorted(result)
    ), "Parts should be sorted when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    # result = split_integer(value=10, number_of_parts=10)
    #   if sum(result) < len(result):

    assert (
        split_integer(value=1, number_of_parts=3) == [0, 0, 1]
    ), "Should add zeros when value is less than number of parts"
