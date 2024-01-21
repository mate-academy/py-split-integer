from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    sum_of_parts = sum(split_integer(32, 6))
    assert sum_of_parts == 32, (
        f"Sum of the parts equal {sum_of_parts}, but it should be equal 32."
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result_of_func = split_integer(6, 2)
    expected_result = [3, 3]
    assert result_of_func == expected_result, (
        f"Result should be list with equal parts {expected_result}, "
        f"got {result_of_func} instead."
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result_of_func = split_integer(32, 1)
    expected_result = [32]
    assert result_of_func == expected_result, (
        f"Result should be list with one element {expected_result}, "
        f"got {result_of_func} instead."
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result_of_func = split_integer(32, 6)
    expected_result = [5, 5, 5, 5, 6, 6]
    assert result_of_func == expected_result, (
        f"Result should be list with sorted data {expected_result}, "
        f"got {result_of_func} instead."
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result_of_func = split_integer(1, 3)
    expected_result = [0, 0, 1]
    assert result_of_func == expected_result, (
        f"Result should be list with zero values {expected_result}, "
        f"got {result_of_func} instead."
    )
