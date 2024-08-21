from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(15, 4)) == 15, (
        "Expected sum to be 15."
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(12, 4)
    assert all(x == result[0] for x in result), (
        f"Expected all parts to be equal, but got {result}."
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8], (
        "Expected [8]."
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == sorted(split_integer(17, 4)), (
        "Expected parts to be sorted."
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(5, 10)
    assert len(result) == 10, (
        "Expected 10 parts."
    )
    assert result.count(0) == 10 - (5 % 10), (
        f"Expected {10 - (5 % 10)} zeros, but got {result.count(0)}."
    )
    assert sum(result) == 5, (
        "Expected sum to be 5."
    )
