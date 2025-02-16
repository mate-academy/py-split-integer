import os
import pytest
from app import split_integer

def test_could_split_on_different_parts(monkeypatch):
    def split_on_equal_part(value: int, number_of_parts: int):
        return [value // number_of_parts] * number_of_parts  # Incorrect logic (ignores remainder)

    monkeypatch.setattr(split_integer, "split_integer", split_on_equal_part)

    assert split_integer.split_integer(10, 3) != [3, 3, 4], "Incorrect implementation should fail"

def test_only_last_number_is_incremented(monkeypatch):
    def split_and_increment_the_last_number(value: int, number_of_parts: int):
        result_list = [value // number_of_parts] * number_of_parts
        if value % number_of_parts != 0:
            result_list[-1] += 1  # Incorrect: should distribute evenly
        return sorted(result_list, reverse=True)  # Incorrect: sorting in reverse order

    monkeypatch.setattr(split_integer, "split_integer", split_and_increment_the_last_number)

    assert split_integer.split_integer(10, 3) != [3, 3, 4], "Incorrect implementation should fail"

def test_split_on_incorrect_parts(monkeypatch):
    def split_on_incorrect_parts(value: int, number_of_parts: int):
        result_list = [value // number_of_parts] * number_of_parts
        for i in range(value % number_of_parts + 1):  # Adds remainder one too many times
            result_list[-1 - i] += 1
        result_list[0] -= 2  # Incorrect: reducing too much
        return result_list

    monkeypatch.setattr(split_integer, "split_integer", split_on_incorrect_parts)

    assert split_integer.split_integer(10, 3) != [3, 3, 4], "Incorrect implementation should fail"

def test_split_on_different_parts(monkeypatch):
    def split_on_different_parts(value: int, number_of_parts: int):
        result_list = [value // number_of_parts] * number_of_parts
        for i in range(value % number_of_parts):
            result_list[-1 - i] += 1
        if value % number_of_parts == 0:
            result_list[0] -= 1  # Incorrect: modifying balanced distribution
            result_list[-1] += 2  # Incorrect: adding too much
        return sorted(result_list, reverse=True)  # Incorrect: sorted in reverse order

    monkeypatch.setattr(split_integer, "split_integer", split_on_different_parts)

    assert split_integer.split_integer(10, 3) != [3, 3, 4], "Incorrect implementation should fail"

def test_no_pass_in_code():
    path_to_tests = os.path.join("app", "test_split_integer.py")
    with open(path_to_tests, "r") as file:
        tests_content = file.read()
        assert "pass" not in tests_content, "Remove 'pass' statements from test cases"
