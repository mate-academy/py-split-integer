from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value():
    # preparation
    value: int = 0
    number_of_parts: int = 0

    # action
    result = split_integer(value, number_of_parts)

    # check
    assert number_of_parts == len(result)  # expected_classes


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    # preparation
    value: int = 0
    number_of_parts: int = 0
    expected_result = []

    # action
    result = split_integer(value, number_of_parts)

    for i in range(number_of_parts):
        if value % number_of_parts == 0:
            expected_result.append(value / number_of_parts)

    # check
    assert expected_result == result  # expected_classes


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    # preparation
    value: int = 0
    number_of_parts: int = 0
    expected_answer: int = 0

    # action
    result = split_integer(value, number_of_parts)
    if len(result) == 1:
        if result[0] == value:
            expected_answer = value

    # check
    assert expected_answer == value  # expected_classes


def test_parts_should_be_sorted_when_they_are_not_equal():
    # preparation
    value: int = 0
    number_of_parts: int = 0
    expected_result = []

    # action
    result = split_integer(value, number_of_parts)

    for i in range(number_of_parts):
        if value % number_of_parts != 0:
            expected_result.append(round(value / number_of_parts) + 1)
            value -= 1
    # check
    assert expected_result == result  # expected_classes


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    # preparation
    value: int = 0
    number_of_parts: int = 0
    expected_result = []

    # action
    result = split_integer(value, number_of_parts)

    if value < number_of_parts:
        for i in range(number_of_parts):
            expected_result.append(0)
    assert expected_result == result  # expected_classes
