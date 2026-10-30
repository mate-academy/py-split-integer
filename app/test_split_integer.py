from app.split_integer import split_integer


def test_result_contains_required_number_of_parts() -> None:
    result = split_integer(17, 4)

    assert len(result) == 4


def test_sum_of_parts_equals_original_value() -> None:
    result = split_integer(17, 4)

    assert sum(result) == 17


def test_result_is_sorted() -> None:
    result = split_integer(17, 4)

    assert result == sorted(result)


def test_difference_between_max_and_min_is_not_more_than_one() -> None:
    result = split_integer(17, 4)

    assert max(result) - min(result) <= 1


def test_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_equal_parts() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_unequal_parts() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_more_parts() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
