from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:

    assert (
        split_integer(8, 1) == [8]
    ), "Value 8 split to 1 part should be equal to [8]"
    assert (
        split_integer(6, 2) == [3, 3]
    ), "Value 6 split to 2 parts should be equal to [3, 3]"
    assert (
        split_integer(17, 4) == [4, 4, 4, 5]
    ), "Value 17 split to 4 parts should be equal to [4, 4, 4, 5]"
    assert (
        split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    ), "Value 32 split to 6 parts should be equal to [5, 5, 5, 5, 6, 6]"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    equal_parts = split_integer(2, 2)
    assert (
        equal_parts[0] == equal_parts[len(equal_parts) - 1]
    ), "Value 2 split to 2 parts should result equal parts of 1"
    equal_parts = split_integer(12, 4)
    assert (
        equal_parts[0] == equal_parts[len(equal_parts) - 1]
    ), "Value 12 split to 4 parts should result equal parts of 3"
    equal_parts = split_integer(100, 25)
    assert (
        equal_parts[0] == equal_parts[len(equal_parts) - 1]
    ), "Value 100 split to 25 parts should result equal parts of 4"
    equal_parts = split_integer(1221, 111)
    assert (
        equal_parts[0] == equal_parts[len(equal_parts) - 1]
    ), "Value 12221 split to 111 parts should result equal parts of 11"
    equal_parts = split_integer(1000000, 100000)
    assert (
        equal_parts[0] == equal_parts[len(equal_parts) - 1]
    ), "Value 1000000 split to 100000 parts should result equal parts of 10"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        len(split_integer(1, 1)) == 1
    ), "Value 1 split to 1 parts should be split into one part"
    assert (
        len(split_integer(52349834583405892, 1)) == 1
    ), "Value 1 split to 1 parts should be split into one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(32, 6) == sorted(split_integer(32, 6))
    ), "Parts should be sorted when they are not equal"
    assert (
        split_integer(777, 8) == sorted(split_integer(777, 8))
    ), "Parts should be sorted when they are not equal"
    assert (
        split_integer(9989989, 322) == sorted(split_integer(9989989, 322))
    ), "Parts should be sorted when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(6, 7) == [0, 1, 1, 1, 1, 1, 1]
    ), "Zeros should be added when the value is less than number of parts"
    assert (
        split_integer(5, 11) == [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    ), "Zeros should be added when the value is less than number of parts"
