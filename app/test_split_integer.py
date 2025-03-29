from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    goals = split_integer(32, 6)
    assert sum(goals) == 32, "sum of the parts should be equal value"


def test_should_split_into_equal_parts_divisible_by_parts() -> None:
    goals = split_integer(16, 4)
    assert goals == [4, 4, 4, 4], "should split into equal parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    goals = split_integer(8, 1)
    assert goals == [8], "should return part equals to value"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    goals = split_integer(32, 6)
    assert goals == [5, 5, 5, 5, 6, 6], \
        "should be sorted when test parts not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    goals = split_integer(1, 3)
    assert goals == [0, 0, 1], \
        "should add zeros when value is less than number of parts"
