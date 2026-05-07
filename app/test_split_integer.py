from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(8, 1)) == 8
    ), "Sum of the parts should be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
            len(set(split_integer(6, 2))) == 1 and
            len(split_integer(6, 2)) == 2
    ), "When the value is divisible by parts, the result should be split into equal parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
            split_integer(17, 1) == [17]
    ), "When split into one part result should return part equals to value"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
            split_integer(32, 6) == sorted(split_integer(32, 6))
    ), "When they are not equal result should be sorted"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
            split_integer(4, 6) == [0,0,1,1,1,1]
    ), "When value is less than number of parts result should should add zeros"
