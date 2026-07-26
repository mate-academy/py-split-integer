from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    parts = split_integer(value=52, number_of_parts=5)
    assert sum(parts) == 52, f"Sum of {parts} should be equal to 52"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts = split_integer(value=10, number_of_parts=2)
    assert (
        all(part == 10 // 2 for part in parts)
    ), f"10 should be equally divided into {parts} when divisible by 2"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    parts = split_integer(value=8, number_of_parts=1)
    assert (
        parts[0] == 8
    ), f"First part {parts[0]} should be equal to 8"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts = split_integer(value=17, number_of_parts=2)
    assert (
        parts == sorted(parts)
    ), f"{parts} should be sorted when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    parts = split_integer(value=1, number_of_parts=2)
    assert (
        len(parts) == 2
    ), f"Expected 2 parts, but got {len(parts)}"

    assert (
        parts == [0, 1]
    ), f"Expected [0, 1], but got {parts}"
