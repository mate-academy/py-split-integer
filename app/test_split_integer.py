from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 32
    number_of_parts = 6
    assert sum(split_integer(value, number_of_parts)) == value


def test_should_return_exact_number_of_parts() -> None:
    value = 6
    number_of_parts = 2
    assert split_integer(value, number_of_parts) == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1
    assert split_integer(value, number_of_parts) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    number_of_parts = 4
    assert split_integer(value, number_of_parts) == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    number_of_parts = 3
    assert split_integer(value, number_of_parts) == [0, 1, 1]


def test_len_of_the_parts_should_be_equal_to_number_of_parts() -> None:
    value = 32
    number_of_parts = 6
    assert len(split_integer(value, number_of_parts)) == number_of_parts


def test_max_min_difference_should_not_exceed_one() -> None:
    value = 32
    number_of_parts = 6
    assert (
        max(split_integer(value, number_of_parts))
        - min(split_integer(value, number_of_parts))
        <= 1
    )
