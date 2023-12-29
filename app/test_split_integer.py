from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:

    assert sum(split_integer(value=17, number_of_parts=5)) == 17


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:

    assert split_integer(value=15, number_of_parts=5) == [3, 3, 3, 3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:

    assert (
        len(split_integer(value=15, number_of_parts=1)) == 1
        and split_integer(value=15, number_of_parts=1)[0] == 15
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:

    assert (
        sorted(split_integer(value=27, number_of_parts=6))
        == split_integer(value=27, number_of_parts=6)
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:

    assert (
        split_integer(value=7, number_of_parts=11)
        == [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
    )
