from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(32, 6)) == 32


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(12, 4) == [3, 3, 3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(1, 3) == [0, 0, 1]
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_should_distribute_remainder_greater_than_one() -> None:
    assert split_integer(18, 4) == [4, 4, 5, 5]
    assert split_integer(10, 3) == [3, 3, 4]
    assert split_integer(11, 3) == [3, 4, 4]
    assert split_integer(100, 7) == [14, 14, 14, 14, 14, 15, 15]


def test_should_split_into_different_number_of_parts() -> None:
    assert split_integer(10, 2) == [5, 5]
    assert split_integer(10, 5) == [2, 2, 2, 2, 2]
    assert split_integer(10, 10) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def test_should_return_exactly_number_of_parts_elements() -> None:
    for value in range(1, 31):
        for number_of_parts in range(1, 31):
            parts = split_integer(value, number_of_parts)
            assert len(parts) == number_of_parts


def test_sum_of_parts_should_be_equal_to_value_for_any_numbers() -> None:
    for value in range(1, 31):
        for number_of_parts in range(1, 31):
            parts = split_integer(value, number_of_parts)
            assert sum(parts) == value


def test_difference_between_max_and_min_should_be_at_most_one() -> None:
    for value in range(1, 31):
        for number_of_parts in range(1, 31):
            parts = split_integer(value, number_of_parts)
            assert max(parts) - min(parts) <= 1


def test_parts_should_be_sorted_ascending_for_any_numbers() -> None:
    for value in range(1, 31):
        for number_of_parts in range(1, 31):
            parts = split_integer(value, number_of_parts)
            assert parts == sorted(parts)
