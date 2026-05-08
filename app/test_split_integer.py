import app.split_integer as split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        isinstance(split_integer.split_integer(13, 4), list)
    ), "Result should be list"
    assert (
        len(split_integer.split_integer(13, 4)) == 4
    ), "Len of the result should be equal to numbers of parts"
    assert (
        sum(split_integer.split_integer(13, 4)) == 13
    ), "Sum of the parts should be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer.split_integer(12, 4) == [3, 3, 3, 3]
    ), (
        "When the value is divisible by parts, "
        "the result should be split into equal parts"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer.split_integer(6, 1) == [6]
    ), "When split into one part result should return part equals to value"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer.split_integer(15, 4) == [3, 4, 4, 4]
    ), "When parts are not equal result should be sorted"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer.split_integer(6, 8) == [0, 0, 1, 1, 1, 1, 1, 1]
    ), "When value is less than number of parts result should should add zeros"


def test_should_split_correctly_when_value_not_divisible_by_parts() -> None:
    assert (
        split_integer.split_integer(17, 4) == [4, 4, 4, 5]
    ), "Parts should be distributed correctly"
