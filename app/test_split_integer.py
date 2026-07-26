from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    test_cases = [
        (10, 3, [3, 3, 4]),
        (25, 5, [5, 5, 5, 5, 5]),
        (7, 2, [3, 4]),
        (0, 1, [0]),
        (100, 10, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
    ]

    for value, parts, expected in test_cases:
        assert split_integer(value, parts) == expected, \
            f"Failed for value={value}, parts={parts}"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    test_cases = [
        (10, 2, [5, 5]),
        (20, 4, [5, 5, 5, 5]),
        (30, 6, [5, 5, 5, 5, 5, 5])
    ]

    for value, parts, expected in test_cases:
        assert split_integer(value, parts) == expected, \
            f"Failed for value={value}, parts={parts}"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    test_cases = [
        (10, [10]),
        (25, [25]),
        (7, [7]),
        (0, [0]),
        (100, [100])
    ]

    for value, expected in test_cases:
        assert split_integer(value, 1) == expected, \
            f"Failed for value={value}"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    test_cases = [
        (10, 3, [3, 3, 4]),
        (25, 4, [6, 6, 6, 7]),
        (7, 2, [3, 4]),
        (11, 5, [2, 2, 2, 2, 3])
    ]

    for value, parts, expected in test_cases:
        assert split_integer(value, parts) == expected, \
            f"Failed for value={value}, parts={parts}"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    test_cases = [
        (2, 5, [0, 0, 0, 1, 1]),
        (3, 7, [0, 0, 0, 0, 1, 1, 1]),
        (0, 4, [0, 0, 0, 0])
    ]

    for value, parts, expected in test_cases:
        assert split_integer(value, parts) == expected, \
            f"Failed for value={value}, parts={parts}"
