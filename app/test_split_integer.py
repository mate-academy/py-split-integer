from app.split_integer import split_integer


def test_sum_of_parts_equals_value() -> None:
    assert sum(split_integer(17, 4)) == 17, \
        "Sum of parts should equal original value"


def test_equal_parts_when_value_divisible() -> None:
    assert split_integer(6, 3) == [2, 2, 2], \
        "Should split into equal parts when divisible"


def test_single_part_equals_value() -> None:
    assert split_integer(8, 1) == [8], \
        "Single part should equal the original value"


def test_parts_sorted_for_unequal_splits() -> None:
    parts = split_integer(17, 4)
    assert parts == sorted(parts), \
        "Parts should be sorted in ascending order"


def test_inclusion_of_zeros_when_value_less_than_parts() -> None:
    assert split_integer(2, 5) == [0, 0, 0, 1, 1], \
        "Should include zeros when value is less than number of parts"
