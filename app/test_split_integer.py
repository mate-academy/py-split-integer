import app.split_integer as split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer.split_integer(17, 4)) == 17
    assert sum(split_integer.split_integer(20, 6)) == 20
    assert sum(split_integer.split_integer(3, 5)) == 3


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer.split_integer(12, 4) == [3, 3, 3, 3]
    assert split_integer.split_integer(20, 5) == [4, 4, 4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer.split_integer(42, 1) == [42]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer.split_integer(17, 4) == [4, 4, 4, 5]


def test_difference_between_max_and_min_should_be_at_most_one() -> None:
    assert max(split_integer.split_integer(17, 4)) - min(
        split_integer.split_integer(17, 4)
    ) <= 1
    assert max(split_integer.split_integer(20, 6)) - min(
        split_integer.split_integer(20, 6)
    ) <= 1


def test_should_have_exact_number_of_parts() -> None:
    assert len(split_integer.split_integer(3, 5)) == 5
    assert len(split_integer.split_integer(20, 6)) == 6


def test_distribution_should_be_as_even_as_possible() -> None:
    value = 14
    parts = 4

    base = value // parts      # 3
    remainder = value % parts  # 2

    result = split_integer.split_integer(value, parts)

    assert result.count(base) == parts - remainder
    assert result.count(base + 1) == remainder


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer.split_integer(3, 5) == [0, 0, 1, 1, 1]
