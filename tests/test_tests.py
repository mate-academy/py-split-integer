from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    for value, parts in [(17, 4), (32, 6), (3, 5), (10, 3)]:
        assert sum(split_integer(value, parts)) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(9, 3) == [3, 3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    for value, parts in [(17, 4), (32, 6), (3, 5)]:
        result = split_integer(value, parts)
        assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(3, 5)
    assert len(result) == 5
    assert sum(result) == 3
    assert min(result) >= 0
    assert max(result) - min(result) <= 1


def test_difference_between_max_and_min_should_be_no_more_than_one() -> None:
    for value, parts in [(17, 4), (32, 6), (10, 3), (5, 5)]:
        result = split_integer(value, parts)
        assert max(result) - min(result) <= 1


def test_should_return_exact_number_of_parts() -> None:
    for value, parts in [(17, 4), (32, 6), (3, 5), (10, 3)]:
        assert len(split_integer(value, parts)) == parts


def test_no_part_should_be_negative() -> None:
    for value, parts in [(17, 4), (3, 5), (10, 3)]:
        assert all(x >= 0 for x in split_integer(value, parts))


def test_all_parts_should_be_integers() -> None:
    for value, parts in [(17, 4), (32, 6), (3, 5)]:
        assert all(isinstance(x, int) for x in split_integer(value, parts))
