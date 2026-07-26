from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 3) == [2, 2, 2]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(10, 1) == [10]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == sorted(split_integer(17, 4))


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert sum(split_integer(4, 6)) == 4
    assert len(split_integer(4, 6)) == 6
    assert split_integer(4, 6).count(0) > 0


def test_should_return_list_with_the_correct_number_of_elements() -> None:
    assert len(split_integer(17, 4)) == 4


def test_difference_between_min_and_max() -> None:
    assert max(split_integer(17, 4)) - min(split_integer(17, 4)) <= 1
