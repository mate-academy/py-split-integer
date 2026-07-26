from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(36, 7)
    assert sum(result) == 36, (
        f"Sum of parts should be equal to 36 but is {sum(result)}"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(42, 6)
    assert result == [7] * 6, (
        f"Number should be divided into equal parts if it is divisible "
        f"by number of parts but actual is {result}"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(17, 1)
    assert result == [17], (
        f"Returned part should be equal to [17] but is {result}"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(27, 5)
    assert result == sorted(result), (
        f"Parts should be sorted from lowest to highest but are {result}"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(3, 5)
    assert result == [0, 0, 1, 1, 1], (
        f"There should be zeros added when the value is less than "
        f"number of parts but actual is {result}"
    )
