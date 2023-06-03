from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:

    assert sum(split_integer(32, 6)) == 32, (
        "The sum of all parts must equal the value!"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:

    assert len(set(split_integer(999, 9))) == 1, (
        "If the test is divided into equal parts,"
        " all the resulting values must be equal!"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:

    assert split_integer(8, 1) == [8], (
        "If the part is one in the "
        "result, it must equal the value!"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(32, 6)
    assert result == sorted(result), (
        "The function must return a sorted list!"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:

    assert split_integer(5, 10)[0:5] == [0, 0, 0, 0, 0], (
        "The function must add zeros when "
        "`value` is less than a `number_of_parts`"
    )
