from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(32, 6)
    assert len(result) == 6
    assert sum(result) == 32
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(17, 1) == [17]


def test_should_be_sorted_and_within_one_difference_for_uneven_split() -> None:
    result = split_integer(17, 4)
    assert len(result) == 4
    assert sum(result) == 17
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_additional_case_checks_for_small_values() -> None:
    result = split_integer(9, 4)
    assert len(result) == 4
    assert sum(result) == 9
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(1, 2) == [0, 1]
