from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    for value, parts in [(8, 3), (17, 4), (32, 6), (5, 10)]:
        result = split_integer(value, parts)
        assert sum(result) == value
        assert len(result) == parts


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]  # приклад з умови
    assert split_integer(12, 4) == [3, 3, 3, 3]
    assert all(x == 3 for x in split_integer(12, 4))


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(100, 1) == [100]


def test_parts_should_be_sorted_and_difference_not_greater_than_one() -> None:
    for value, parts in [(17, 4), (32, 6), (7, 3), (10, 4)]:
        result = split_integer(value, parts)
        assert result == sorted(result), f"{result} is not sorted"
        assert max(result) - min(result) <= 1


def test_extra_ones_should_go_to_last_parts() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(3, 5)
    assert result == [0, 0, 1, 1, 1]
    assert sum(result) == 3
    assert len(result) == 5


def test_difference_between_any_two_numbers_is_at_most_one() -> None:
    for value in range(1, 30):
        for parts in range(1, value + 2):
            result = split_integer(value, parts)
            diffs = [abs(a - b) for a in result for b in result]
            assert all(d <= 1 for d in diffs), f"Too large diff in {result}"
