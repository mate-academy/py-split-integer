from app import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer.split_integer(17, 4)) == 17
    assert sum(split_integer.split_integer(32, 6)) == 32
    assert sum(split_integer.split_integer(6, 2)) == 6


def test_length_of_returned_list_should_match_number_of_parts() -> None:
    assert len(split_integer.split_integer(17, 4)) == 4
    assert len(split_integer.split_integer(2, 5)) == 5
    assert len(split_integer.split_integer(32, 6)) == 6


def test_max_min_difference_is_at_most_one() -> None:
    parts_1 = split_integer.split_integer(32, 6)
    assert max(parts_1) - min(parts_1) <= 1

    parts_2 = split_integer.split_integer(17, 4)
    assert max(parts_2) - min(parts_2) <= 1

    parts_3 = split_integer.split_integer(6, 2)
    assert max(parts_3) - min(parts_3) <= 1


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer.split_integer(6, 2) == [3, 3]
    assert split_integer.split_integer(100, 4) == [25, 25, 25, 25]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer.split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer.split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer.split_integer(32, 6) == [5, 5, 5, 5, 6, 6]

    parts = split_integer.split_integer(17, 4)
    assert parts == sorted(parts)

    parts_large = split_integer.split_integer(32, 6)
    assert parts_large == sorted(parts_large)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer.split_integer(2, 5) == [0, 0, 0, 1, 1]
