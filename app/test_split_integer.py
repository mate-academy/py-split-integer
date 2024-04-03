from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    initial_value = 32
    number_of_parts = 6
    assert sum(split_integer(initial_value, number_of_parts)) == initial_value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    initial_value = 16
    number_of_parts = 4
    assert len(set(split_integer(initial_value, number_of_parts))) == 1


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    initial_value = 8
    number_of_parts = 1
    assert split_integer(initial_value, number_of_parts)[0] == initial_value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    initial_value = 16
    number_of_parts = 4
    assert (split_integer(initial_value, number_of_parts) ==
            sorted(split_integer(initial_value, number_of_parts)))


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    initial_value = 6
    number_of_parts = 10
    diff = number_of_parts - initial_value
    assert split_integer(initial_value, number_of_parts)[:diff] == [0] * diff
