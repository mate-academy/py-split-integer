from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    # split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    value = 32
    number_of_parts = 6

    parts = split_integer(value, number_of_parts)

    assert max(parts) - min(parts) <= 1


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    # split_integer(30, 6) == [5, 5, 5, 5, 5, 5]
    value = 30
    number_of_parts = 6
    check = True

    parts = split_integer(value, number_of_parts)

    for i in range(len(parts) - 1):
        if parts[i] != parts[i + 1]:
            check = False

    assert check



def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    # split_integer(9, 1) == [9]
    value = 9
    number_of_parts = 1

    parts = split_integer(value, number_of_parts)

    assert parts == [value]


def test_parts_should_be_sorted_when_they_are_not_equal():
    # split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    value = 32
    number_of_parts = 6
    check = True

    parts = split_integer(value, number_of_parts)

    for i in range(len(parts) - 1):
        if parts[i] > parts[i + 1]:
            check = False

    assert check


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    # split_integer(4, 6) == [0, 0, 1, 1, 1, 1]
    value = 4
    number_of_parts = 6

    parts = split_integer(value, number_of_parts)

    assert parts == [0, 0, 1, 1, 1, 1]
