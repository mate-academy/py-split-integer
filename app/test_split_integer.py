from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(8, 4)
    assert sum(result) == 8, "Sum of 'parts' should be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(15, 3)
    assert result == [5, 5, 5], ("Parts should equal to each other"
                                 " if value divisible by parts")


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(3, 1)
    assert result == [3], \
        "Part should equal to value when split into one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(14, 3)
    assert result == [4, 5, 5], \
        "Parts should be sorted when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(1, 2)
    assert result == [0, 1], \
        "Add zeros when value is less than number of parts"
