from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(36, 7)) == 36, (
        f"Sum of parts should be equal to 36 "
        f"but is {sum(split_integer(36, 7))}"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(42, 6) == [7] * 6, (
        f"Number should be divided into equal parts if it is divisible "
        f"by number of parts but actual is {(split_integer(36, 7))}"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(17, 1) == [17], (
        f"Returned part should be equal to [17] "
        f"but is {(split_integer(36, 7))}"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(27, 5) == sorted(split_integer(27, 5)), (
        f"Parts should be sorted from lowest to highest "
        f"but are {(split_integer(36, 7))}"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1], (
        f"There should be zeros added when the value is less than "
        f"number of parts but actual is {(split_integer(36, 7))}"
    )
