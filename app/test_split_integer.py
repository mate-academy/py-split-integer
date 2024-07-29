from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(17, 4)) == 17,
        "Sum number_of_parts should be equal to 17"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(6, 3)
    assert (
        all(part == result[0] for part in result),
        "All parts should be equal when value is divisible by number_of_parts"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(8, 1)
    assert len(result) == 1, "There should be exactly one part"
    assert result[0] == 8, "The single part should be equal to the 8"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(32, 6)
    sort_result = sorted(result)
    assert (
        sort_result == [5, 5, 5, 5, 6, 6],
        "The parts should be sorted in ascending order."
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    parts = split_integer(3, 5)
    assert (
        parts == [0, 0, 0, 1, 2],
        "Expected result: parts should be distributed in ascending order."
        " For value=3 and number_of_parts=5, the split should result in: [0, 0, 0, 1, 2]"
    )
