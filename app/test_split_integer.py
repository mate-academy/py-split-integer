from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    number_of_parts = 4
    assert (
        sum(split_integer(value, number_of_parts)) == value,
        "Sum of the parts should be equal to `value`"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    number_of_parts = 2
    assert (
        split_integer(value, number_of_parts) == [3, 3],
        "'value' should be splited into equal parts when value divisible by parts"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1
    assert (
        split_integer(value, number_of_parts) == [8],
        "Should return part equals to value when split into one part"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 32
    number_of_parts = 6
    assert (
        split_integer(value, number_of_parts) == [5, 5, 5, 5, 6, 6],
        "Parts should be sorted when they are not equal"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    number_of_parts = 3
    assert (
        split_integer(value, number_of_parts) == [0, 1, 1],
        "Should add zeros when value is less than number of parts"
    )
