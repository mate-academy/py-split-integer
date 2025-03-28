from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    test_cases = [
        (8, 10),
        (10, 2),
        (10, 3),
        (10, 5),
        (0, 1),
        (7, 7),
        (15, 10)
    ]

    for value, number_of_parts in test_cases:
        parts = split_integer(value, number_of_parts)
        total = sum(parts)

        assert total == value, \
            f"Sum of the {parts} should be equal to the {value}"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    test_cases = [
        (10, 2),
        (10, 3),
        (10, 5),
        (0, 1),
        (7, 7),
        (15, 10)
    ]

    for value, number_of_parts in test_cases:
        parts = split_integer(value, number_of_parts)

        assert len(parts) == number_of_parts, \
            f"Should split into {number_of_parts} parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    test_cases = [
        (10, 1),
        (5, 1),
        (0, 1),
        (7, 1),
        (15, 1)
    ]

    for value, number_of_parts in test_cases:
        parts = split_integer(value, number_of_parts)

        assert parts == [value], f"Should return [{value}], but got {parts}"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    test_cases = [
        (10, 2),
        (10, 3),
        (10, 5),
        (0, 1),
        (7, 7),
        (15, 10)
    ]

    for value, number_of_parts in test_cases:
        parts = split_integer(value, number_of_parts)

        assert parts == sorted(parts), \
            f"{parts} should be sorted when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    test_cases = [
        (10, 2),
        (10, 3),
        (10, 5),
        (0, 1),
        (7, 7),
        (15, 10)
    ]

    for value, number_of_parts in test_cases:
        parts = split_integer(value, number_of_parts)

        assert len(parts) == number_of_parts, \
            f"Should add zeros when {value} is less than number of {parts}"
