from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(10, 3)
    assert sum(result) == 10, (
        "Sum of the parts should be equal to value."
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(16, 4)
    assert len(set(result)) == 1, (
        "should split into equal parts when value divisible by parts."
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(7, 1)
    assert result == [7], (
        "should return part equals to value when split into one part."
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(18, 5)
    assert result == sorted(result), (
        "parts should be sorted when they are not equal."
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(2, 5)
    assert result.count(0) == 3, (
        "Should add zeros when value is less than the number of parts."
    )
