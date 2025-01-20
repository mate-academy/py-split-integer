from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    input_val = 19
    parts = 3
    assert split_integer(input_val, parts) == [6,6,7]


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    input_val = 25
    parts = 5
    assert split_integer(input_val, parts) == [5,5,5,5,5]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(10, 1) == [10]



def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    input_val = 26
    parts = 6
    assert split_integer(input_val, parts) == [4,4,4,4,5,5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    input_val = 2
    parts = 5
    assert split_integer(input_val, parts) == [0,0,0,1,1]
