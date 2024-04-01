from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 32
    number_of_parts = 7
    func_ = split_integer(value, number_of_parts)

    assert sum(func_) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 18
    number_of_parts = 3
    func_ = split_integer(value, number_of_parts)

    assert func_[0] == func_[1] == func_[2]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 18
    number_of_parts = 1
    func_ = split_integer(value, number_of_parts)

    assert func_[0] == value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 20
    number_of_parts = 3
    func_ = split_integer(value, number_of_parts)

    assert func_[0] <= func_[1] <= func_[2]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    number_of_parts = 4
    func_ = split_integer(value, number_of_parts)

    assert func_[1] == 0
