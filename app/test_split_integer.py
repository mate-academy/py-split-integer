from app import split_integer


def test_single_part_returns_value() -> None:
    assert split_integer.split_integer(8, 1) == [8]


def test_divisible_case() -> None:
    assert split_integer.split_integer(5, 5) == [1, 1, 1, 1, 1]


def test_remainder_distribution_17_4() -> None:
    assert split_integer.split_integer(17, 4) == [4, 4, 4, 5]


def test_remainder_distribution_32_6() -> None:
    assert split_integer.split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_value_less_than_parts() -> None:
    assert split_integer.split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_result_properties() -> None:
    result = split_integer.split_integer(17, 4)

    assert len(result) == 4
    assert sum(result) == 17
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
