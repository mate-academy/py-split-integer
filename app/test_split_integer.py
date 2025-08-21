from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value, number_of_parts = 10, 3
    result = split_integer(value, number_of_parts)
    assert sum(result) == value, ("Sum of parts should be "
                                  "equal to the original value")


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value, number_of_parts = 12, 4
    result = split_integer(value, number_of_parts)
    assert all(part == 3 for part in result), \
        "All parts should be equal when divisible"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value, number_of_parts = 8, 1
    result = split_integer(value, number_of_parts)
    assert result == [8], \
        "Should return the value itself when splitting into one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value, number_of_parts = 17, 4
    result = split_integer(value, number_of_parts)
    assert result == sorted(result), \
        "Parts should be sorted in ascending order"


def test_difference_between_max_and_min_should_be_at_most_one() -> None:
    value, number_of_parts = 20, 6
    result = split_integer(value, number_of_parts)
    assert max(result) - min(result) <= 1, \
        "Difference between max and min should be at most 1"


def test_all_elements_should_be_integers() -> None:
    value, number_of_parts = 17, 4
    result = split_integer(value, number_of_parts)
    assert all(isinstance(x, int) for x in result), \
        "All elements should be integers"


def test_result_length_should_equal_number_of_parts() -> None:
    value, number_of_parts = 20, 6
    result = split_integer(value, number_of_parts)
    assert len(result) == number_of_parts, \
        "Length of result should equal number_of_parts"


def test_example_case_split_integer_32_6() -> None:
    result = split_integer(32, 6)
    assert result == [5, 5, 5, 5, 6, 6], \
        "Should match the example case from the description"


def test_should_not_always_split_into_equal_parts() -> None:
    result = split_integer(10, 3)
    assert result == sorted(result), "Parts should always be sorted"
    assert sum(result) == 10, "Sum of parts should match value"
    assert max(result) - min(result) <= 1, "Difference should be at most 1"


def test_should_not_decrease_first_element_unnecessarily() -> None:
    result = split_integer(9, 3)
    assert result[0] >= 3, "First element should not be unnecessarily reduced"
