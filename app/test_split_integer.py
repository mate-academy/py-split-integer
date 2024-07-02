from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17, "sum of the parts are not equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert len(set(split_integer(12, 4))) == 1, "all parts should be equal"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1)[0] == 8, "when the part is single it should be equal to value"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(32, 6)
    assert result == sorted(result), "parts should be sorted when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 4).count(0) == 2, "zeros should be added if value less than number_of_parts"
