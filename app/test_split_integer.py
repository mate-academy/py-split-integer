from app import split_integer as si


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    print("__name__ = ", __name__)
    assert sum(si.split_integer(17, 4)) == 17


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert si.split_integer(10, 5) == [10 // 5] * 5


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert si.split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert sorted(si.split_integer(32, 6)) == si.split_integer(32, 6)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert si.split_integer(3, 4) == [0, 1, 1, 1]
