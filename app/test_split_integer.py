from app.split_integer import split_integer
import pytest


def test_split_on_incorrect_parts(monkeypatch: str) -> None:
    def split_on_incorrect_parts(value: int, number_of_parts: int) -> None:
        result_list = [value // number_of_parts] * number_of_parts
        for i in range(value % number_of_parts + 1):
            result_list[-1 - i] += 1
        result_list[0] -= 1
        return result_list
    monkeypatch.setattr("app.split_integer.split_integer",
                        split_on_incorrect_parts)
    test_result = pytest.main(["app/test_split_integer.py"])
    monkeypatch.undo()
    assert test_result.value != 0, (
        "Function 'split_on_incorrect_parts' shouldn't pass all tests"
    )


def test_split_on_different_parts(monkeypatch: str) -> None:
    def split_on_different_parts(value: int, number_of_parts: int) -> None:
        result_list = [value // number_of_parts] * number_of_parts
        for i in range(value % number_of_parts):
            result_list[-1 - i] += 1
        if value % number_of_parts == 0:
            result_list[0] -= 1
            result_list[-1] += 1
        return result_list

    monkeypatch.setattr("app.split_integer.split_integer",
                        split_on_different_parts)
    test_result = pytest.main(["app/test_split_integer.py"])
    monkeypatch.undo()
    assert test_result.value != 0, (
        "Function 'split_on_different_parts' shouldn't pass all tests"
    )


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
