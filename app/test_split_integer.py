import app.split_integer as split_integer_module


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    parts = 4

    result = split_integer_module.split_integer(value, parts)

    assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 12
    parts = 4

    result = split_integer_module.split_integer(value, parts)

    assert result == [3, 3, 3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 9

    result = split_integer_module.split_integer(value, 1)

    assert result == [9]


def test_parts_should_be_sorted_and_difference_should_be_at_most_one() -> None:
    value = 17
    parts = 4

    result = split_integer_module.split_integer(value, parts)

    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_should_distribute_remainder_correctly() -> None:
    value = 17
    parts = 4

    result = split_integer_module.split_integer(value, parts)

    base = value // parts
    remainder = value % parts

    assert result.count(base + 1) == remainder
    assert result.count(base) == parts - remainder


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 3
    parts = 5

    result = split_integer_module.split_integer(value, parts)

    assert len(result) == parts
    assert sum(result) == value
    assert result.count(0) == parts - value
    assert result == sorted(result)


def test_should_have_elements_greater_than_base_when_there_is_remainder(
) -> None:
    value = 7
    parts = 3

    result = split_integer_module.split_integer(value, parts)

    base = value // parts

    assert any(x > base for x in result)


def test_should_split_integer_using_reference_examples() -> None:
    assert split_integer_module.split_integer(8, 1) == [8]
    assert split_integer_module.split_integer(6, 2) == [3, 3]
    assert split_integer_module.split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer_module.split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    assert split_integer_module.split_integer(7, 3) == [2, 2, 3]
