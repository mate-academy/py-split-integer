import pytest

from app import split_integer


def test_could_split_on_different_parts(monkeypatch):
    def split_on_equal_part(value: int, number_of_parts: int):
        return [value // number_of_parts] * number_of_parts

    monkeypatch.setattr(split_integer, "split_integer", split_on_equal_part)

    test_result = pytest.main(["../app/test_split_integer.py"])
    assert (
        test_result.value == 1
    ), "Function 'split_on_equal_part' shouldn't pass all tests"


def test_only_last_number_is_incremented(monkeypatch):
    def split_and_increment_the_last_number(value: int, number_of_parts: int):
        result_list = [value // number_of_parts] * number_of_parts
        if value % number_of_parts != 0:
            result_list[-1] += 1
        return result_list

    monkeypatch.setattr(
        split_integer, "split_integer", split_and_increment_the_last_number
    )

    test_result = pytest.main(["../app/test_split_integer.py"])
    assert (
        test_result.value == 1
    ), "Function 'split_and_increment_the_last_number' shouldn't pass all tests"


def test_split_on_incorrect_parts(monkeypatch):
    def split_on_incorrect_parts(value: int, number_of_parts: int):
        result_list = [value // number_of_parts] * number_of_parts
        for i in range(value % number_of_parts + 1):
            result_list[-1 - i] += 1
        result_list[0] -= 1
        return result_list

    monkeypatch.setattr(split_integer, "split_integer", split_on_incorrect_parts)

    test_result = pytest.main(["../app/test_split_integer.py"])
    assert (
        test_result.value == 1
    ), "Function 'split_on_incorrect_parts' shouldn't pass all tests"


def test_split_on_different_parts(monkeypatch):
    def split_on_different_parts(value: int, number_of_parts: int):
        result_list = [value // number_of_parts] * number_of_parts
        for i in range(value % number_of_parts):
            result_list[-1 - i] += 1
        if value % number_of_parts == 0:
            result_list[0] -= 1
            result_list[-1] += 1
        return result_list

    monkeypatch.setattr(split_integer, "split_integer", split_on_different_parts)

    test_result = pytest.main(["../app/test_split_integer.py"])
    assert (
        test_result.value == 1
    ), "Function 'split_on_different_parts' shouldn't pass all tests"
