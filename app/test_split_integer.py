from app.split_integer import split_integer


def test_single_part_returns_value() -> None:
    assert split_integer(8, 1) == [8]


def test_even_split() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_basic_uneven_split() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_larger_uneven_split() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_result_length() -> None:
    assert len(split_integer(20, 5)) == 5


def test_sum_is_correct() -> None:
    assert sum(split_integer(19, 4)) == 19


def test_is_sorted() -> None:
    result = split_integer(23, 5)
    assert result == sorted(result)


def test_difference_at_most_one() -> None:
    result = split_integer(25, 4)
    assert max(result) - min(result) <= 1


def test_exact_distribution_case_1() -> None:
    assert split_integer(10, 3) == [3, 3, 4]


def test_exact_distribution_case_2() -> None:
    assert split_integer(20, 6) == [3, 3, 3, 3, 4, 4]


def test_exact_distribution_case_3() -> None:
    assert split_integer(7, 3) == [2, 2, 3]


def test_remainder_must_be_distributed() -> None:
    value = 7
    parts = 3
    result = split_integer(value, parts)

    assert sum(result) == value
    assert len(set(result)) > 1


def test_remainder_elements_at_end() -> None:
    value = 20
    parts = 6
    result = split_integer(value, parts)

    base = value // parts
    remainder = value % parts

    first_part = [base] * (parts - remainder)
    second_part = [base + 1] * remainder

    assert result[: parts - remainder] == first_part
    assert result[parts - remainder:] == second_part


def test_no_wrong_distribution() -> None:
    value = 17
    parts = 4
    result = split_integer(value, parts)

    base = value // parts

    assert all(x >= base for x in result)
    assert all(x <= base + 1 for x in result)
