from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(10, 5)
    assert len(result) == 5, \
        "Length of the result should be equal to number_of_parts"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 17
    parts = 4
    result = split_integer(value, parts)
    assert sum(result) == value, \
        "Sum of all parts should equal the original value"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(10, 1)
    assert result == sorted(result),\
        "Resulting list should be sorted in ascending order"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 32
    parts = 6
    result = split_integer(value, parts)
    assert max(result) - min(result) <= 1, \
        "Difference between max and min should be at most 1"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(3, 5)
    assert sum(result) == 3
    assert len(result) == 5
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_strict_conditions() -> None:
    test_cases = [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (10, 3),
        (100, 9),
    ]

    for value, parts in test_cases:
        result = split_integer(value, parts)

        assert len(result) == parts, "Incorrect number of parts"
        assert sum(result) == value, "Sum of parts not equal to value"
        assert result == sorted(result), "Parts are not sorted ascending"
        assert (
            max(result) - min(result) <= 1
        ), "Difference between max and min parts greater than 1"

        base = value // parts
        remainder = value % parts

        bigger_parts_count = sum(
            1 for x in result if x == base + 1
        )
        smaller_parts_count = sum(
            1 for x in result if x == base
        )

        assert bigger_parts_count == remainder, (
            "Incorrect number of bigger parts"
        )
        assert smaller_parts_count == parts - remainder, (
            "Incorrect number of smaller parts"
        )
