from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(20, 4)) == 20


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    ext = split_integer(30, 5)
    assert len(ext) == 5


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    ext = split_integer(12, 1)
    assert ext == [12]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    ext = split_integer(34, 7)
    assert ext == sorted(ext)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    ext = split_integer(7, 9)
    assert ext == [0, 0, 1, 1, 1, 1, 1, 1, 1]
