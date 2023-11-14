from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 21
    number_of_parts = 3
    assert sum(split_integer(value, number_of_parts)) == value, (
        "Sum of the parts should be equal to value!"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(6, 2)
    assert all(result[i - 1] == result[i] for i in range(1, len(result))), (
        "Should split into equal parts when value divisible by parts!"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 11
    number_of_parts = 1
    result = split_integer(value, number_of_parts)
    assert result[0] == value, (
        "Should return part equals to value when split into one part!"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(45, 2)
    assert result == sorted(result), (
        "Parts should be sorted when they are not equal!"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 4) == [0, 1, 1, 1], (
        "Should add zeros when value is less than the number of parts!"
    )
