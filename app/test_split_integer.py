from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    cases = [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (3, 5),
        (100, 9),
    ]
    for value, parts in cases:
        result = split_integer(value, parts)
        assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    cases = [
        (6, 2, 3),
        (12, 4, 3),
        (100, 5, 20),
    ]
    for value, parts, expected_each in cases:
        result = split_integer(value, parts)
        assert result == [expected_each] * parts


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(123, 1) == [123]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)  # e.g. [4, 4, 4, 5]
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value, parts = 3, 5
    result = split_integer(value, parts)
    # Must be sorted and sum to value
    assert result == sorted(result)
    assert sum(result) == value
    # When value < parts, minimal-diff integer split uses 0s and 1s
    assert min(result) == 0
    assert max(result) in (0, 1)
    assert result.count(0) == parts - value
    assert result.count(1) == value
