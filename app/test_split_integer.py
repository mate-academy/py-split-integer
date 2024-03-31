from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value, number_of_parts = 6, 2
    assert (sum(split_integer(value, number_of_parts)) == 6
            ), "sum of the result list should be equal to start value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value, number_of_parts = 110, 10
    assert (split_integer(value, number_of_parts)
            == [11, 11, 11, 11, 11, 11, 11, 11, 11, 11]
            ), ("if start value divisible by number_of_parts, "
                "all parts should be equal")


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value, number_of_parts = 13, 1
    assert (split_integer(value, number_of_parts) == [13]
            ), "should return list of start value if number_of_parts == 1"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value, number_of_parts = 17, 4
    assert (split_integer(value, number_of_parts) == [4, 4, 4, 5]
            ), "return should be a sorted list if parts are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value, number_of_parts = 2, 5
    assert (split_integer(value, number_of_parts) == [0, 0, 0, 1, 1]
            ), ("return should have number of zeros inside equal to "
                "'number_of_parts - value' if value < number_of_parts")
