import pytest
from app.split_integer import split_integer  # Импортируем функцию

# Тест: проверка случая с одним элементом
def test_split_integer_single_part():
    assert split_integer(8, 1) == [8]

# Тест: проверка равного деления на 2 части
def test_split_integer_two_parts_equal():
    assert split_integer(6, 2) == [3, 3]

# Тест: проверка, когда результат нужно распределить с разницей 1
def test_split_integer_multiple_parts_with_remainder():
    assert split_integer(17, 4) == [4, 4, 4, 5]

# Тест: проверка сортировки и равномерного распределения
def test_split_integer_larger_number():
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]

# Тест: проверка минимальной разницы между max и min
def test_split_integer_max_min_difference():
    result = split_integer(10, 3)
    assert max(result) - min(result) <= 1

# Тест: проверка сортировки (возрастание)
def test_split_integer_sorted():
    result = split_integer(20, 6)
    assert result == sorted(result)

# Тест: проверка на случай, когда число делится идеально
def test_split_integer_exact_division():
    result = split_integer(12, 4)
    assert result == [3, 3, 3, 3]