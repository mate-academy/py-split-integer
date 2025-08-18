from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(10, 3)) == 10
    assert sum(split_integer(25, 5)) == 25
    assert sum(split_integer(7, 7)) == 7
    # Boundary condition
    assert sum(split_integer(1, 1)) == 1
    # Large value
    large_result = split_integer(10_000, 3)
    assert sum(large_result) == 10_000


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(12, 4) == [3, 3, 3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
    # Additional boundary
    assert split_integer(0, 5) == [0, 0, 0, 0, 0]
    assert split_integer(5, 10) == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]


def test_required_examples() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_max_min_difference() -> None:
    for value, parts in [(10, 3), (17, 4), (32, 6), (6, 2), (7, 7)]:
        result = split_integer(value, parts)
        assert max(result) - min(result) <= 1
