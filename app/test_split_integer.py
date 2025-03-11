from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(6, 2)
    assert sum(result) == 6,\
        "Sum of the parts should be equal to 6"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(6, 2)
    assert result == [3, 4],\
        "Parts should be equal when value divisible py parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(8, 1)
    assert result == [8],\
        "Part should be equal to value when split into one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(32, 6)
    assert result == sorted(result),\
        "Parts should be sorted when they aren't equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(5, 10)
    assert result.count(0) > 0,\
        "Zeros should be in list when value is less than number of parts"
