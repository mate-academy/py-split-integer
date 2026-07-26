import pytest
from app.split_integer import split_integer

def test_only_last_number_is_incremented():
    """
    Проверяет случай, когда остаток распределяется по порядку.
    """
    assert split_integer(10, 3) == [4, 3, 3]

def test_split_on_different_parts():
    """
    Проверяет равномерное распределение остатков.
    """
    assert split_integer(10, 4) == [3, 3, 2, 2]

def test_should_handle_value_less_than_parts():
    """
    Проверяет случай, когда value меньше числа частей.
    """
    assert split_integer(3, 5) == [1, 1, 1, 0, 0]

def test_no_sorting_of_parts():
    """
    Проверяет порядок распределения остатков.
    """
    assert split_integer(13, 4) == [4, 3, 3, 3]