from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(10, 3)) == 10,\
        "The sum of the parts should equal the value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(12, 4) == [3, 3, 3, 3],\
        ("Does not split value into equal"
         "parts when divisible by number of parts")


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8],\
        ("Should return a single part equal"
         "to the value when number of parts is 1")


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    assert result == sorted(result),\
        "Parts should be sorted in ascending order"
    assert max(result) - min(result) <= 1,\
        "Difference between max and min elements should be ≤ 1"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1],\
        "Should add zeros when value is less than number of parts"
