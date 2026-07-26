from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    for value, parts in [(8, 3), (17, 4), (32, 6), (50, 7),
                         (100, 9), (200, 15)]:
        assert sum(split_integer(value, parts)) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    for value, parts in [(6, 2), (12, 3), (20, 5),
                         (100, 10), (200, 20)]:
        result = split_integer(value, parts)
        assert result == [value // parts] * parts


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    for value in [8, 15, 99, 150, 300]:
        assert split_integer(value, 1) == [value]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    for value, parts in [(17, 4), (32, 6), (22, 5), (41, 8),
                         (99, 7), (150, 9)]:
        result = split_integer(value, parts)
        assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    for value, parts in [(3, 5), (2, 4), (5, 10),
                         (7, 15), (1, 3)]:
        result = split_integer(value, parts)
        assert sum(result) == value and all(x in [0, 1] for x in result)


def test_max_min_difference_should_not_exceed_one() -> None:
    for value, parts in [(10, 3), (20, 7), (15, 4),
                         (30, 6), (100, 9), (200, 15)]:
        result = split_integer(value, parts)
        assert max(result) - min(result) <= 1


def test_result_should_be_sorted() -> None:
    for value, parts in [(19, 4), (25, 5), (40, 8),
                         (50, 7), (99, 6), (150, 10)]:
        result = split_integer(value, parts)
        assert result == sorted(result)


def test_correct_number_of_parts() -> None:
    for value, parts in [(10, 3), (20, 7), (15, 4),
                         (30, 6), (99, 9), (200, 20)]:
        result = split_integer(value, parts)
        assert len(result) == parts


def test_all_elements_are_positive_or_zero() -> None:
    for value, parts in [(10, 3), (20, 7), (5, 10),
                         (7, 15), (1, 3), (99, 9)]:
        result = split_integer(value, parts)
        assert all(x >= 0 for x in result)


def test_number_of_parts_equals_value() -> None:
    for value in [1, 2, 3, 4, 5, 10, 15, 20]:
        result = split_integer(value, value)
        assert result == [1] * value
