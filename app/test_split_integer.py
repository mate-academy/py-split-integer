from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    data = ((6, 2), (17, 4), (32, 6))
    for value, number_of_parts in data:
        assert sum(split_integer(value, number_of_parts)) == value


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    data = ((6, 2), (17, 4), (32, 6))
    for value, number_of_parts in data:
        assert len(split_integer(value, number_of_parts)) == number_of_parts


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    value = 8
    assert sum(split_integer(value, 1)) == value


def test_parts_should_be_sorted_when_they_are_not_equal():
    result = split_integer(35, 6)
    for i in range(1, len(result)):
        assert result[i] >= result[i - 1]


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    result = split_integer(5, 6)
    assert result[0] == 0


def test_difference_between_max_and_min_number():
    data = ((6, 2), (17, 4), (32, 6))
    for value, number_of_parts in data:
        min_value = min(split_integer(value, number_of_parts))
        max_value = max(split_integer(value, number_of_parts))
        assert max_value - min_value <= 1
