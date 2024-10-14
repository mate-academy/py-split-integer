from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(6, 2)
    assert sum(result) == 6, f"sum of {result} should be equal {6}"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(6, 2)
    assert result == [3, 3], f"{result} should be split on equal parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(5, 1)
    assert result == [5], f"should be equal to value when split {1}. Exemple: {result}"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(5, 4) == [1, 1, 1, 2], "parts should be sorted when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(1, 5)
    assert result == [0, 0, 0, 0, 1], f"should add zeros when value is less than number of part. Exemple: {result}"


def test_some_bad_test_for_pytest_tests() -> None:
    assert False
