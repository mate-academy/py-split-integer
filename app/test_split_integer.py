from app.split_integer import split_integer


def test_single_part() -> None:
    assert split_integer(8, 1) == [8]


def test_divisible_cases() -> None:
    assert split_integer(12, 3) == [4, 4, 4]


def test_remainder_distribution() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(5, 3) == [1, 2, 2]
    assert split_integer(10, 4) == [2, 2, 3, 3]
    assert split_integer(17, 2) == [8, 9]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_edge_cases() -> None:
    assert split_integer(2, 5) == [0, 0, 0, 1, 1]
    assert split_integer(0, 3) == [0, 0, 0]


def test_general_properties() -> None:
    res = split_integer(17, 4)
    assert len(res) == 4
    assert sum(res) == 17
    assert res == sorted(res)
    assert max(res) - min(res) <= 1


def test_specific_small_and_edge_cases() -> None:
    assert split_integer(1, 2) == [0, 1]
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
    assert split_integer(4, 2) == [2, 2]
    assert split_integer(9, 3) == [3, 3, 3]
    assert split_integer(6, 4) == [1, 1, 2, 2]
    assert split_integer(7, 7) == [1, 1, 1, 1, 1, 1, 1]


def test_reject_bad_increment_only_right() -> None:
    def bad_split(value: int, number_of_parts: int) -> list:
        base = value // number_of_parts
        res = [base] * number_of_parts
        for i in range(value % number_of_parts):
            res[-1 - i] += 1
        return res

    res = bad_split(3, 5)
    assert len(res) == 5
    assert sum(res) == 3
    assert res == sorted(res)
    assert max(res) - min(res) <= 1


def test_reject_bad_shifted() -> None:
    def bad_split2(value: int, number_of_parts: int) -> list:
        base = value // number_of_parts
        res = [base] * number_of_parts
        for i in range(value % number_of_parts + 1):
            res[-1 - i] += 1
        res[0] -= 1
        return res

    res = bad_split2(3, 5)
    assert not (
        len(res) == 5
        and sum(res) == 3
        and res == sorted(res)
        and max(res) - min(res) <= 1
    )


def test_reject_shifted_distribution() -> None:
    def bad2(value: int, parts: int) -> list:
        base = value // parts
        res = [base] * parts
        for i in range(value % parts + 1):
            res[-1 - i] += 1
        res[0] -= 1
        return res

    cases = [(2, 4), (4, 3), (5, 4), (6, 4), (2, 5)]

    for v, p in cases:
        r = bad2(v, p)
        assert len(r) == p, f"bad2 returned wrong length for {(v, p)}"
        sum_ok = sum(r) == v
        sorted_ok = r == sorted(r)
        diff_ok = (max(r) - min(r) <= 1)
        assert not (len(r) == p and sum_ok and sorted_ok and diff_ok), (
            f"bad2  for case {(v, p)} with result {r}"
        )
