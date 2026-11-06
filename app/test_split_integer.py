import app.split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(app.split_integer.split_integer(17, 4)) == 17
    assert sum(app.split_integer.split_integer(32, 6)) == 32


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert app.split_integer.split_integer(6, 2) == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert app.split_integer.split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert app.split_integer.split_integer(17, 4) == [4, 4, 4, 5]
    assert app.split_integer.split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
