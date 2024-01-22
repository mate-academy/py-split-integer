from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    number_of_parts = 4
    assert (
            sum(split_integer(value, number_of_parts)) == value
    ), f"The sum of parts should be {value}"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    number_of_parts = 2
    func_result = split_integer(value, number_of_parts)
    assert split_integer(6, 2) == [3, 3], (
        "Function should split value into equal parts"
    )
    # assert (
    #     func_result[0:int(number_of_parts/2)] == func_result[int(number_of_parts/2):]
    # ), f"Each element in result {func_result} should be {value/number_of_parts} "


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1
    assert (
        split_integer(value, number_of_parts) == [value]
    ), f"Should return {value}"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 32
    number_of_parts = 6
    func_result = split_integer(value, number_of_parts)
    assert (
        sorted(func_result) == func_result
    ), f"Should be sorted {sorted(func_result)}"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 1
    number_of_parts = 2
    assert (
           split_integer(1, 2) == [0, 1]
    ), "Should return 0 inside array"
