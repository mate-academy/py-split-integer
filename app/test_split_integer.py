from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    for value, number_of_parts in [(8, 1), (6, 2), (17, 4), (32, 6)]:
        result = split_integer(value, number_of_parts)
        assert sum(result) == value, \
            f"Sum of parts {result} should equal {value}"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    for value, number_of_parts in [(6, 2), (8, 4), (10, 5)]:
        result = split_integer(value, number_of_parts)
        assert all(x == result[0] for x in result), \
            f"All parts {result} should be equal to {result[0]}"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    for value in [1, 5, 10, 100]:
        result = split_integer(value, 1)
        assert result == [value], f"Result {result} should equal to [{value}]"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    for value, number_of_parts in [(17, 4), (32, 6), (10, 3)]:
        result = split_integer(value, number_of_parts)
        assert result == sorted(result), f"Parts {result} should be sorted"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    for value, number_of_parts in [(1, 2), (2, 3), (3, 5)]:
        result = split_integer(value, number_of_parts)

        expected_result = [0] * (number_of_parts - value) + [1] * value
        assert result == expected_result, \
            f"Result {result} should be {expected_result}"
