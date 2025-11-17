from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(10, 3)) == 10


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(12, 3) == [4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(7, 1) == [7]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(10, 4)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(3, 5)
    assert len(result) == 5
    assert sum(result) == 3
    assert result == sorted(result)


def test_difference_between_adjacent_elements_not_greater_than_one() -> None:
    result = split_integer(10, 4)
    for first, second in zip(result, result[1:]):
        assert abs(first - second) <= 1


def test_remainder_is_distributed_to_last_positions() -> None:
    value, parts = 10, 4
    res = split_integer(value, parts)

    base = value // parts
    remainder = value % parts

    assert res[: parts - remainder] == [base] * (parts - remainder)
    assert res[parts - remainder :] == [base + 1] * remainder
