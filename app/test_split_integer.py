from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(20, 6)) == 20
    assert sum(split_integer(8, 2)) == 8,\
        "Sum of the parts should be equal to start integer value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(4, 2)[0] == split_integer(4, 2)[1]
    assert split_integer(8, 2)[0] == split_integer(8, 2)[1],\
        "Parts should be equal when value divisible by parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1)[0] == 8, \
        "Parts should have one value equal to start when split into one"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(8, 3) == sorted(split_integer(8, 3)),\
        "Parts should be sorted when they are not_equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(4, 6)[0] == 0,\
        "parts should starts with 0 if value less than number of parts"
