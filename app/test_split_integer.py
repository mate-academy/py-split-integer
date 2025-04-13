from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    test_cases = [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (10, 3),
        (5, 5)
    ]

    for value, number_of_parts in test_cases:
        result = split_integer(value, number_of_parts)
        assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(8, 4) == [2, 2, 2, 2]
    assert split_integer(15, 3) == [5, 5, 5]
    assert split_integer(100, 4) == [25, 25, 25, 25]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(42, 1) == [42]
    assert split_integer(0, 1) == [0]
    assert split_integer(1000, 1) == [1000]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result1 = split_integer(17, 4)
    result2 = split_integer(32, 6)
    result3 = split_integer(10, 3)

    assert result1 == [4, 4, 4, 5]
    assert result2 == [5, 5, 5, 5, 6, 6]
    assert result3 == [3, 3, 4]

    # Check that each result is sorted
    for result in [result1, result2, result3]:
        assert result == sorted(result)


def test_max_min_difference_should_be_at_most_one() -> None:
    test_cases = [
        (17, 4),
        (32, 6),
        (10, 3),
        (11, 3),
        (7, 2),
        (99, 10)
    ]

    for value, number_of_parts in test_cases:
        result = split_integer(value, number_of_parts)
        assert max(result) - min(result) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(0, 3) == [0, 0, 0]
    assert split_integer(2, 5) == [0, 0, 0, 1, 1]
    assert split_integer(1, 3) == [0, 0, 1]
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
