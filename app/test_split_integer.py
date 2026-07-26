from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(18, 4)) == 18


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(16, 4) == [16 / 4 for _ in range(4)]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert sorted(split_integer(32, 6)) == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 4) == [0, 0, 1, 1]


def test_differnce_between_the_max_and_min_should_be_not_mor_one() -> None:
    assert max(split_integer(32, 6)) - min(split_integer(32, 6)) <= 1


def test_long_mast_be_equal_value() -> None:
    assert len(split_integer(21, 4)) == 4
