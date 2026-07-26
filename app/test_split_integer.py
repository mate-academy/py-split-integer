from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    func = split_integer(10, 5)
    assert sum(func) == 10



def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    func = split_integer(9, 3)
    assert len(func) == 3
    assert func == [3, 3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    func = split_integer(7, 1)
    assert func == [7]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    func = split_integer(10, 3)
    assert func == [3, 3, 4]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    func = split_integer(2, 3)
    assert func == [0, 1, 1]
