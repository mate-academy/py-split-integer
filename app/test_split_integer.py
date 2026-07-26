from app.split_integer import split_integer


def test_core_logic_result() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_sum_of_parts_equals_value() -> None:
    assert sum(split_integer(10, 3)) == 10
    assert sum(split_integer(2, 5)) == 2


def test_difference_between_max_and_min_is_at_most_one() -> None:
    assert max(split_integer(20, 6)) - min(split_integer(20, 6)) <= 1
    assert max(split_integer(10, 5)) - min(split_integer(10, 5)) <= 1


def test_parts_are_sorted_ascending() -> None:
    assert split_integer(20, 6) == sorted(split_integer(20, 6))


def test_length_of_result_equals_number_of_parts() -> None:
    assert split_integer(10, 3) == [3, 3, 4]
    assert split_integer(5, 5) == [1, 1, 1, 1, 1]


def test_split_into_one_part_is_value_itself() -> None:
    assert split_integer(8, 1) == [8]


def test_value_less_than_parts_contains_zeros() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_element_type_is_int() -> None:
    assert all(isinstance(x, int) for x in split_integer(10, 3))


def test_all_parts_non_negative() -> None:
    assert all(x >= 0 for x in split_integer(3, 5))


def test_even_divisibility() -> None:
    assert split_integer(12, 3) == [4, 4, 4]


def test_uneven_divisibility() -> None:
    assert split_integer(5, 3) == [1, 2, 2]
