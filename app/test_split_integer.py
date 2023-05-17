from app.split_integer import split_integer
import copy


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value, number_of_parts = 14, 3
    elements = split_integer(value, number_of_parts)
    total = 0
    for element in elements:
        total += element
    assert (
        total == value
    ), f"Sum of the parts should be equal to {value}"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value, number_of_parts = 12, 3
    elements = split_integer(value, number_of_parts)
    assert (
        all(element == elements[0] for element in elements)
    ), f"If {value} is divided without the remainder by {number_of_parts}, elements should be equal parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value, number_of_parts = 15, 1
    elements = split_integer(value, number_of_parts)
    assert (
            len(elements) == 1 and value in elements
    ), f"If number of parts is 1, should return part equals to value"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value, number_of_parts = 17, 3
    elements = split_integer(value, number_of_parts)
    sorted_elements = copy.copy(elements)
    sorted_elements.sort()
    assert (
            not all(element == elements[0] for element in elements) and elements == sorted_elements
    ), f"Parts should be sorted when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value, number_of_parts = 3, 6
    elements = split_integer(value, number_of_parts)
    assert (
            0 in elements
    ), f"Should add zeros when value is less than number of parts"
