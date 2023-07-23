from app.split_integer import split_integer
from app.support import splitting_list_into_two_equal_parts


def test_sum_of_the_parts_equal_to_value() -> None:
    assert sum(split_integer(15, 3)) == 15


def test_split_equal_when_value_divisible_by_parts() -> None:
    left, right = splitting_list_into_two_equal_parts(split_integer(12, 4))
    assert left == right


def test_split_value_on_different_parts() -> None:
    left, right = splitting_list_into_two_equal_parts(split_integer(17, 5))
    assert left < right


def test_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(10, 1) == [10]


def test_parts_sorted_when_they_are_not_equal() -> None:
    """
    With my solution this test is redundant.
    My test "split_value_on_different_parts" checks it also.
    At least it seems so to me. :)
    """

    assert split_integer(11, 3) == sorted(split_integer(11, 3))


def test_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(1, 3) == [0, 0, 1]


def test_is_split_integer_length_correct() -> None:
    assert len(split_integer(100, 64)) == 64


def test_split_when_just_last_one_number_biggest() -> None:
    element = split_integer(10, 3)
    assert element[-1] == min(element) + 1
