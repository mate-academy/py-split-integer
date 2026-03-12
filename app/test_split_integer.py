from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    cases = [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
    ]
    for value, parts in cases:
        result = list(split_integer(value, parts))
        assert isinstance(result, list)
        assert len(result) == parts
        assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    cases = [
        (6, 2),
        (8, 4),
        (10, 5),
    ]
    for value, parts in cases:
        result = list(split_integer(value, parts))
        assert len(result) == parts
        assert len(set(result)) == 1
        assert sum(result) == value


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    cases = [
        (6, 1),
        (8, 1),
        (10, 1),
    ]
    for value, parts in cases:
        result = list(split_integer(value, parts))
        assert len(result) == parts
        assert sum(result) == value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    cases = [
        (8, 3),
        (6, 4),
        (17, 4),
        (32, 5),
    ]
    for value, parts in cases:
        result = list(split_integer(value, parts))
        assert isinstance(result, list)
        assert len(result) == parts
        assert result == sorted(result)
        assert len(set(result)) > 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    cases = [
        (2, 3),
        (6, 8),
        (1, 3),
    ]
    for value, parts in cases:
        result = list(split_integer(value, parts))
        assert isinstance(result, list)
        assert len(result) == parts
        assert result == sorted(result)
        assert result[0] == 0
        assert max(result) - min(result) <= 1
