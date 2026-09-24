from app.split_integer import split_integer


def test_could_split_on_different_parts() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_when_first_part_less_than_last_part_on_one() -> None:
    assert max(split_integer(17,4)) - min(split_integer(17,4)) <= 1
    assert max(split_integer(32, 6)) - min(split_integer(32, 6)) <= 1


def test_only_last_number_is_incremented() -> None:
    result = split_integer(17, 4)
    assert result[0] < result[-1]


def test_split_on_incorrect_parts() -> None:
    assert split_integer(10, 5) == [2,2,2,2,2]


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(100, 5) == [20, 20, 20, 20, 20]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8,1 ) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17,4) == sorted(split_integer(17, 4))

def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 5) == [0, 0, 0, 1, 1]
    assert len(split_integer(2, 5)) == 5
