from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    parts = split_integer(6, 2) # [3, 3]
    result_sum = 0
    for number in parts:
        result_sum += number
    assert result_sum == 6



def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts = split_integer(9, 3) # [3, 3, 3]
    assert parts[0] == parts[1] == parts[2]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    parts = split_integer(8, 1) # [8]
    assert parts[0] == 8


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts = split_integer(17, 4) # [4, 4, 4, 5]
    assert parts == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    parts = split_integer(1, 4) #[1, 0, 0, 0]
    assert parts == [1, 0, 0, 0]
