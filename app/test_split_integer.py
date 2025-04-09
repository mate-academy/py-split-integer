from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    test_cases = [
        (7, 3),
        (10, 5),
        (100, 9),
        (25, 4),
    ]
    for value, number_of_parts in test_cases:
        parts = split_integer(value, number_of_parts)
        assert sum(parts) == value, (
            f"For value={value} and parts={number_of_parts}, "
            f"expected sum {value}, but got {sum(parts)} with parts {parts}"
        )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(25, 5) == [5, 5, 5, 5, 5]
    assert split_integer(25, 7) == [3, 3, 3, 4, 4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    test_cases = [
        (9, 1),
        (10, 1),
        (100, 1),
        (25, 1),
    ]
    for value, number_of_parts in test_cases:
        parts = split_integer(value, number_of_parts)
        assert len(parts) == 1 and parts[0] == value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    test_cases = [
        (7, 3),
        (10, 5),
        (100, 9),
        (25, 4),
    ]
    for value, number_of_parts in test_cases:
        parts = split_integer(value, number_of_parts)
        assert sorted(parts) == parts


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 7) == [0, 0, 0, 0, 1, 1, 1]
    assert split_integer(5, 10) == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    assert split_integer(2, 4) == [0, 0, 1, 1]
