from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value, parts = 17, 4
    result = split_integer(value, parts)
    assert sum(result) == value, ("The sum of the parts "
                                  "should be equal to the original value")


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value, parts = 6, 2
    result = split_integer(value, parts)
    assert len(set(result)) == 1, ("All parts should be "
                                   "equal when value is divisible by parts")


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value, parts = 8, 1
    result = split_integer(value, parts)
    assert result == [value], ("Should return a list with "
                               "the original value when split into one part")


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value, parts = 17, 4
    result = split_integer(value, parts)
    assert result == sorted(result), ("Parts should "
                                      "be sorted in ascending order")


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value, parts = 2, 5
    result = split_integer(value, parts)
    assert result.count(0) == parts - value, ("Should add zeros "
                                              "when value is less "
                                              "than number of parts")
