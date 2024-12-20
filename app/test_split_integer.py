from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(10, 3)
    assert (sum(result) == 10),\
        f"Expected sum of parts to be 10, got {sum(result)}"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(12, 3)
    assert (result == [4, 4, 4])\
        , f"Expected parts to be [4, 4, 4], got {result}"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(7, 1)
    assert result == [7], f"Expected parts to be [7], got {result}"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    assert result == [4, 4, 4, 5],\
        f"Expected parts to be [4, 4, 4, 5], got {result}"
    assert result == sorted(result),\
        "Parts are not sorted in ascending order"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(3, 5)
    assert result == [0, 0, 1, 1, 1],\
        f"Expected parts to be [0, 0, 1, 1, 1], got {result}"
    assert sum(result) == 3,\
        f"Expected sum of parts to be 3, got {sum(result)}"
