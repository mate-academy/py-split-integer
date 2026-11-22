from app.split_integer import split_integer


def test_should_return_whole_value_when_one_part_requested() -> None:
    assert split_integer(8, 1) == [8]


def test_should_split_into_equal_parts_when_value_divides_evenly() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_should_split_17_into_4_parts_exactly() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_should_split_32_into_6_parts_exactly() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_return_exactly_number_of_parts_elements() -> None:
    assert len(split_integer(17, 4)) == 4


def test_should_return_parts_that_sum_up_to_value() -> None:
    assert sum(split_integer(32, 6)) == 32


def test_should_have_difference_between_max_and_min_at_most_one() -> None:
    result = split_integer(32, 6)

    assert max(result) - min(result) <= 1


def test_should_return_parts_sorted_ascending() -> None:
    result = split_integer(17, 4)

    assert result == sorted(result)


def test_should_return_all_ones_when_value_equals_number_of_parts() -> None:
    assert split_integer(5, 5) == [1, 1, 1, 1, 1]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
