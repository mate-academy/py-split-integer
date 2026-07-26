from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    test_cases = [
        (8, 1), (6, 2), (17, 4), (32, 6), (10, 3), (3, 5)
    ]
    for value, parts in test_cases:
        assert sum(split_integer(value, parts)) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    test_cases = [
        (6, 2, [3, 3]),
        (10, 5, [2, 2, 2, 2, 2]),
        (30, 3, [10, 10, 10])
    ]
    for value, parts, expected in test_cases:
        assert split_integer(value, parts) == expected


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(100, 1) == [100]


def test_parts_should_be_sorted_and_difference_at_most_one() -> None:
    test_cases = [(17, 4), (32, 6), (20, 6), (1, 10), (10, 3)]
    for value, parts in test_cases:
        assert (split_integer(value, parts)
                == sorted(split_integer(value, parts)))
        assert (max(split_integer(value, parts))
                - min(split_integer(value, parts)) <= 1)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
    assert split_integer(1, 10) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]


def test_remainder_should_be_distributed_to_last_elements_only() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    assert split_integer(20, 6) == [3, 3, 3, 3, 4, 4]
    assert split_integer(10, 3) == [3, 3, 4]
    assert split_integer(5, 10) == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]


def test_length_of_result_should_equal_number_of_parts() -> None:
    for value, parts in [(10, 3), (25, 7), (5, 10), (100, 1)]:
        assert len(split_integer(value, parts)) == parts
