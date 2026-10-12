from app.split_integer import split_integer


def test_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_split_into_equal_parts() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_split_into_four_parts() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_split_into_six_parts() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_result_has_correct_number_of_parts() -> None:
    result = split_integer(20, 3)
    assert len(result) == 3


def test_result_is_sorted_ascending() -> None:
    result = split_integer(17, 4)
    assert result == sorted(result)


def test_difference_between_max_and_min_is_at_most_one() -> None:
    result = split_integer(17, 4)
    assert max(result) - min(result) <= 1


def test_sum_of_parts_equals_original_value() -> None:
    result = split_integer(17, 4)
    assert sum(result) == 17
