import app.split_integer as split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value, parts = 17, 4
    result = split_integer.split_integer(value, parts)
    assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer.split_integer(6, 2) == [3, 3]
    assert split_integer.split_integer(12, 3) == [4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer.split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer.split_integer(17, 4)
    assert result == sorted(result)


def test_example_32_6_matches_spec() -> None:
    assert split_integer.split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_result_contains_exactly_number_of_parts() -> None:
    value, parts = 19, 5
    result = split_integer.split_integer(value, parts)
    assert len(result) == parts


def test_all_elements_are_integers() -> None:
    result = split_integer.split_integer(17, 4)
    assert all(isinstance(x, int) for x in result)


def test_range_difference_between_min_and_max_is_at_most_one() -> None:
    for value, parts in [(17, 4), (32, 6)]:
        result = split_integer.split_integer(value, parts)
        assert max(result) - min(result) <= 1
