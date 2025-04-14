import pytest
from app.split_integer import split_integer


def test_single_part():
    """Перевірка, що для одного розділу функція повертає масив з єдиним елементом."""
    assert split_integer(8, 1) == [8]


def test_even_split():
    """Перевірка рівномірного поділу: 6 на 2 частини має дати [3, 3]."""
    assert split_integer(6, 2) == [3, 3]


def test_uneven_split():
    """Перевірка нерівномірного поділу із різницею не більше 1."""
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_sorted_order():
    """Перевірка, що масив відсортовано за зростанням."""
    result = split_integer(32, 6)
    assert result == sorted(result)


def test_max_min_difference():
    """Перевірка, що різниця між максимальним і мінімальним елементом не перевищує 1."""
    test_cases = [
        (17, 4),
        (32, 6),
        (100, 7),
        (25, 3),
    ]
    for value, parts in test_cases:
        result = split_integer(value, parts)
        assert max(result) - min(result) <= 1, (
            f"Для значення {value} і {parts} частин отримано {result}"
        )


def test_sum_equals_original_value():
    """Перевірка, що сума елементів масиву дорівнює початковому значенню."""
    test_cases = [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (100, 7),
        (25, 3),
    ]
    for value, parts in test_cases:
        result = split_integer(value, parts)
        assert sum(result) == value, (
            f"Для значення {value} і {parts} частин отримано суму {sum(result)}"
        )
