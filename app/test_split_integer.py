from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(8, 1)) == 8
    assert sum(split_integer(6, 2)) == 6
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(32, 6)) == 32


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(8, 1)
    assert len(result) == 1
    assert result[0] == 8
    result = split_integer(6, 2)
    assert len(result) == 2
    assert result[0] == 3
    assert result[1] == 3
    result = split_integer(17, 4)
    assert len(result) == 4
    assert result[0] == 4
    assert result[1] == 4
    assert result[2] == 4
    assert result[3] == 5
    result = split_integer(32, 6)
    assert len(result) == 6
    assert result[0] == 5
    assert result[1] == 5
    assert result[2] == 5
    assert result[3] == 5
    assert result[4] == 6
    assert result[5] == 6


def test_difference_between_max_and_min() -> None:
    result = split_integer(17, 4)
    assert max(result) - min(result) <= 1


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(3, 5)
    assert result == [0, 0, 1, 1, 1]


def test_value_equals_parts() -> None:
    result = split_integer(5, 5)

    assert len(result) == 5
    assert sum(result) == 5
    assert max(result) - min(result) <= 1


def test_large_value_distribution() -> None:
    result = split_integer(100, 3)

    assert len(result) == 3
    assert sum(result) == 100
    assert max(result) - min(result) <= 1


def test_value_less_than_parts() -> None:
    result = split_integer(2, 5)

    assert len(result) == 5
    assert sum(result) == 2
    assert max(result) - min(result) <= 1
    assert result == sorted(result)


def test_remainder_distribution_exact() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_exact_known_cases() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(8, 1) == [8]


def test_another_exact_case() -> None:
    assert split_integer(10, 3) == [3, 3, 4]
