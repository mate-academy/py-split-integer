from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    test_cases = [
        (10, 3),
        (25, 5),
        (7, 2),
        (0, 1),
        (100, 10)
    ]

    for value, parts in test_cases:
        result = split_integer(value, parts)
        assert sum(result) == value, f"Failed for value={value}, parts={parts}, got {result}"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    test_cases = [
        (10, 2),
        (20, 4),
        (30, 6)
    ]

    for value, parts in test_cases:
        result = split_integer(value, parts)
        expected_part = value // parts
        assert all(x == expected_part for x in result), f"Failed for value={value}, parts={parts}, got {result}"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    test_cases = [10, 25, 7, 0, 100]

    for value in test_cases:
        result = split_integer(value, 1)
        assert result == [value], f"Failed for value={value}, got {result}"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    test_cases = [
        (10, 3),
        (25, 4),
        (7, 2),
        (11, 5)
    ]

    for value, parts in test_cases:
        result = split_integer(value, parts)
        assert result == sorted(result), f"Failed for value={value}, parts={parts}, got {result}"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    test_cases = [
        (2, 5),
        (3, 7),
        (0, 4)
    ]

    for value, parts in test_cases:
        result = split_integer(value, parts)
        assert len(result) == parts, f"Failed for value={value}, parts={parts}, got {result}"
        assert result.count(
            0) == parts - value, f"Failed zero distribution for value={value}, parts={parts}, got {result}"
