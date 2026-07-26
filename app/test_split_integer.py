from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(4, 2)) == 4, (
        f"Expected sum to be 4, but got {sum(split_integer(4, 2))}"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(4, 2)[0] == split_integer(4, 2)[1], (
        "Parts are not equal as expected"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(10, 1)[0] == 10, (
        "The single part should be equal to the value"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6], (
        "Parts are not sorted correctly"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 5) == [0, 0, 0, 1, 1], (
        "Incorrect parts for value < parts"
    )
