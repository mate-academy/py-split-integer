from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(32, 3)) == 32


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (split_integer(33, 3)) == [11, 11, 11]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(32, 1) == [32]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(12, 3)
    assert sorted(result) == result


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(5, 6) == [0, 1, 1, 1, 1, 1]


def test_example_split_8_1() -> None:
    assert split_integer(8, 1) == [8]


def test_example_split_6_2() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_example_split_17_4() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_example_split_32_6() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
