import random
from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = random.randint(10, 1000)
    parts = random.randint(1, 10)
    assert (sum(split_integer(value, parts)) == value), \
        "Sum of the parts should be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    part_value = random.randint(10, 1000)
    parts = random.randint(1, 10)
    value = part_value * parts
    assert (split_integer(value, parts) == [part_value] * parts), \
        "Should split into equal parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = random.randint(10, 1000)
    assert (split_integer(value, 1) == [value]), \
        "Should return part equals to value"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    assert max(result) - min(result) <= 1
    assert \
        (result == [4, 4, 4, 5]), \
        "Parts should be sorted"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = random.randint(1, 10)
    parts = random.randint(10, 20)
    tested_list = split_integer(value, parts)
    zeroes = [0 for _ in range(parts, value, -1)]
    assert (len(tested_list) == parts)
    for index, item in enumerate(tested_list):
        if index < len(zeroes):
            assert (item == zeroes[index]), \
                "Should add zeros when value is less than number of parts"
        else:
            assert (item != 0), \
                "Should add zeros when value is less than number of parts"
