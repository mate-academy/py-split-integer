from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(6, 2)
    assert sum(result) == 6
    assert result == [3, 3]
    result1 = split_integer(17, 4)
    assert sum(result1) == 17
    assert result1 == [4, 4, 4, 5]


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result2 = split_integer(13, 3)
    assert result2 == [4, 4, 5]
    assert len(result2) == 3
    assert max(result2) - min(result2) <= 1
    assert all(isinstance(x, int) for x in result2)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8], \
        "Parts should return equals to value when split into one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6],\
        "Parts should be sorted when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result1 = split_integer(3, 5)
    assert result1 == [0, 0, 1, 1, 1]
    assert max(result1) - min(result1) <= 1
    assert all(isinstance(x, int) for x in result1)
