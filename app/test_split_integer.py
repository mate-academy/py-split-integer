from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 6
    number_of_parts = 2
    assert sum(split_integer(value, number_of_parts)) == value,\
        "Sum of the parts should be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    expected_result = [5, 5, 5, 5, 6, 6]
    assert min(expected_result) != max(expected_result)\
        or min(expected_result) + 1 != max(expected_result), \
        "Split not into equal parts when value divisible by parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    expected_result = [8]
    value = 8
    number_of_parts = 1
    assert split_integer(value, number_of_parts) == expected_result \
           and len(expected_result) == 1, \
           f"if 'number_of_parts' equals_to {number_of_parts} should return 'value'"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    expected_result = [4, 4, 4, 5]
    assert expected_result == sorted(expected_result), \
        "Parts should be sorted when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    expected_result = [1, 1, 1, 0]
    value = 3
    number_of_parts = 4
    assert sum(split_integer(value, number_of_parts)) == value and len(expected_result) == number_of_parts, \
        "Should add zeros"
