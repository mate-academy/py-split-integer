from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(8, 1)
    assert result == [8]
    assert len(result) == 1
    assert all(isinstance(x, int) for x in result)


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(6, 2)
    assert result == [3, 3]
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(6, 1)
    assert result == [6]
    assert len(result) == 1
    assert all(isinstance(x, int) for x in result)


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(32, 6)
    assert result == [5, 5, 5, 5, 6, 6]
    assert len(result) == 6
    assert all(isinstance(x, int) for x in result)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(3, 4)
    assert result == [0, 1, 1, 1]
    assert len(result) == 4
    assert all(isinstance(x, int) for x in result)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_difference_between_max_and_min_should_be_at_most_one() -> None:
    result = split_integer(17, 4)
    base = 17 // 4
    rem = 17 % 4
    assert result == [4, 4, 4, 5]
    assert len(result) == 4
    assert all(isinstance(x, int) for x in result)
    assert all(x in {base, base + 1} for x in result)
    assert result.count(base + 1) == rem
    assert result == sorted(result)
    assert sum(result) == 17


def test_split_integer_remainder_one_case() -> None:
    result = split_integer(7, 4)
    base = 7 // 4
    rem = 7 % 4
    assert result == [1, 2, 2, 2]
    assert len(result) == 4
    assert all(isinstance(x, int) for x in result)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    assert all(x in {base, base + 1} for x in result)
    assert result.count(base + 1) == rem


def test_split_integer_minimal_value_case() -> None:
    result = split_integer(1, 3)
    assert result == [0, 0, 1]
    assert len(result) == 3
    assert all(isinstance(x, int) for x in result)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    assert sum(result) == 1
