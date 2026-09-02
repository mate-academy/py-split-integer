from app import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    for value, parts in [(8, 1), (6, 2), (17, 4), (32, 6), (19, 4), (100, 7)]:
        result = split_integer.split_integer(value, parts)
        assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer.split_integer(6, 2)
    assert result == [3, 3]

    result = split_integer.split_integer(20, 4)
    assert result == [5, 5, 5, 5]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer.split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    for value, parts in [(17, 4), (32, 6), (19, 4), (7, 3)]:
        result = split_integer.split_integer(value, parts)
        assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer.split_integer(2, 5) == [0, 0, 0, 1, 1]


def test_difference_between_max_and_min_should_be_at_most_one() -> None:
    for value, parts in [(17, 4), (32, 6), (19, 4), (13, 4), (100, 7), (2, 5)]:
        result = split_integer.split_integer(value, parts)
        assert max(result) - min(result) <= 1


def test_result_length_should_equal_number_of_parts() -> None:
    for value, parts in [(8, 1), (6, 2), (17, 4), (32, 6)]:
        result = split_integer.split_integer(value, parts)
        assert len(result) == parts
