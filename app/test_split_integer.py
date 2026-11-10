from app.split_integer import split_integer


def test_sum_or_count_is_correct() -> None:
    assert split_integer(8, 1) == [8]


def test_moves_to_single_array_if_complete_parts_is_one() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_should_split_into_equal_parts_when_value_is_divisible() -> None:
    assert split_integer(15, 3) == [5, 5, 5]


def test_should_return_part_differ_by_at_most_one() -> None:
    result = split_integer(17, 4)
    assert max(result) - min(result) <= 1


def test_should_return_exact_split_for_seventeen_into_four_parts() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]

