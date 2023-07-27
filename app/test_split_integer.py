from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = sum(split_integer(32, 6))
    assert result == 32, (
        "Test failed: The sum of the parts is not equal to the original value."
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(15, 3)
    assert result == [5, 5, 5], (
        f"Test failed: Expected [5, 5, 5], but got {result}. "
        "All integers in list must be 5."
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(8, 1)[0]
    assert result == 8, f"Test failed: Expected [8], but got {result}."


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(32, 6)
    resault_sorted = sorted(result)
    assert result == resault_sorted, (
        f"Test failed: {result} must be sorted. {result} != {resault_sorted}"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(1, 19)
    correct_resaul = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    assert result == correct_resaul, (
        f"Test failed: Expected list [0], but got {result}."
    )