from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    # [4, 4, 4, 5])
    assert sum(split_integer(17, 4)) == 17


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(10, 2) == [5, 5]
    assert split_integer(12, 3) == [4, 4, 4]
    assert split_integer(20, 4) == [5, 5, 5, 5]

    #split_integer(8, 1) == [8]
    #split_integer(6, 2) == [3, 3]
    #split_integer(17, 4) == [4, 4, 4, 5]
    #split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(10, 1) == [10]
    assert split_integer(50, 1) == [50]
    assert split_integer(100, 1) == [100]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    assert split_integer(13, 4) == [3, 3, 3, 4]
    assert split_integer(11, 3) == [3, 4, 4]
    assert split_integer(5, 5) == [1, 1, 1, 1, 1]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(1, 5) == [0, 0, 0, 0, 1]
    assert split_integer(2, 4) == [0, 0, 1, 1]


def test_difference_between_max_and_min_number_in_array_should_be_1() -> None:
    max_number = max(split_integer(17, 4))
    min_number = min(split_integer(17, 4))
    assert max_number - min_number <= 1
