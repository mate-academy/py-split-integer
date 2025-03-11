from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(8, 3)) == 8,\
        "Sum of the parts should be equal to 8"
    assert sum(split_integer(25, 5)) == 25,\
        "Sum of the parts should be equal to 25"
    assert sum(split_integer(10, 2)) == 10,\
        "Sum of the parts should be equal to 10"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3],\
        "Expected: [3, 3], but got a different result"
    assert split_integer(12, 4) == [3, 3, 3, 3],\
        "Expected: [3, 3, 3, 3], but got a different result"
    assert split_integer(100, 5) == [20, 20, 20, 20, 20],\
        "Expected: [20, 20, 20, 20, 20], but got a different result"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8],\
        "Part should be equal to value when split into one part"
    assert split_integer(42, 1) == [42],\
        "Part should be equal to value when split into one part"
    assert split_integer(100, 1) == [100], \
        "Part should be equal to value when split into one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5],\
        "Parts should be sorted when they aren`t equal. "
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6],\
        "Parts should be sorted when they aren`t equal. "
    assert split_integer(20, 3) == [6, 7, 7],\
        "Parts should be sorted when they aren`t equal. "


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 5) == [0, 0, 0, 1, 1],\
        "Zeros should be in list when value is less than number of parts. "
    assert split_integer(3, 7) == [0, 0, 0, 0, 1, 1, 1],\
        "Zeros should be in list when value is less than number of parts. "
    assert split_integer(1, 3) == [0, 0, 1],\
        "Zeros should be in list when value is less than number of parts. "
