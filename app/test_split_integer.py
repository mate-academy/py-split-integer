import app.split_integer as split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    for value, parts in [(17, 4), (20, 6), (3, 5), (100, 9)]:
        result = split_integer.split_integer(value, parts)
        assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    for value, parts in [(12, 4), (20, 5), (100, 10)]:
        result = split_integer.split_integer(value, parts)
        assert result == [value // parts] * parts


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer.split_integer(42, 1)
    assert result == [42]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer.split_integer(17, 4)
    assert result == sorted(result)


def test_difference_between_max_and_min_should_be_at_most_one() -> None:
    for value, parts in [(17, 4), (20, 6), (101, 10), (5, 4)]:
        result = split_integer.split_integer(value, parts)
        assert max(result) - min(result) <= 1


def test_should_have_exact_number_of_parts() -> None:
    for value, parts in [(3, 5), (20, 6), (100, 9)]:
        result = split_integer.split_integer(value, parts)
        assert len(result) == parts


def test_distribution_should_be_as_even_as_possible() -> None:
    value = 14
    parts = 4
    result = split_integer.split_integer(value, parts)

    base = value // parts
    remainder = value % parts

    assert result.count(base) == parts - remainder
    assert result.count(base + 1) == remainder


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer.split_integer(3, 5)
    assert result == [0, 0, 1, 1, 1]
