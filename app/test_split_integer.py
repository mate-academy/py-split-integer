from app.main import split_integer


def test_should_return_single_element_when_parts_equal_one() -> None:
    assert split_integer(8, 1) == [8]


def test_should_split_evenly_when_value_divides_exactly() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_should_distribute_remainder_by_adding_one() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_should_return_sorted_array() -> None:
    result: list[int] = split_integer(32, 6)

    assert result == sorted(result)


def test_difference_between_min_and_max_should_be_at_most_one() -> None:
    result: list[int] = split_integer(32, 6)

    assert max(result) - min(result) <= 1


def test_should_return_exact_number_of_parts() -> None:
    result: list[int] = split_integer(32, 6)

    assert len(result) == 6
