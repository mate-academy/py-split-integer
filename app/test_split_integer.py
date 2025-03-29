from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(8, 2)
    assert sum(result) == 8, (f"Expected sum to be 8, but got {sum(result)} "
                              f"for result {result}")


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(6, 2)
    assert result == [3, 3], f"Expected [3, 3] but got {result}"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(1, 1)
    assert result == [1], f"Expected result to be 1, but got {result}"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(5, 3)
    assert result == sorted(result), (f"Expected result to be sorted but got"
                                      f" {result}")


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(3, 4)
    expected_result = [0, 1, 1, 1]
    assert result == expected_result, (f"Expected result to be "
                                       f"{expected_result} but got "
                                       f"{result}")
