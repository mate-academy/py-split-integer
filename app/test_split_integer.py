import app.split_integer


def test_split_into_one_part() -> None:
    """Перевірка розділення на 1 частину."""
    assert app.split_integer.split_integer(8, 1) == [8]
    assert app.split_integer.split_integer(99, 1) == [99]


def test_split_equal_parts() -> None:
    """Перевірка рівномірного ділення без залишку."""
    assert app.split_integer.split_integer(6, 2) == [3, 3]
    assert app.split_integer.split_integer(20, 4) == [5, 5, 5, 5]


def test_parts_difference_is_at_most_one() -> None:
    """Перевірка, що різниця між елементами не перевищує 1."""
    assert app.split_integer.split_integer(17, 4) == [4, 4, 4, 5]
    assert app.split_integer.split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_result_is_sorted_ascending() -> None:
    """Перевірка сортування за зростанням."""
    res1 = app.split_integer.split_integer(17, 4)
    res2 = app.split_integer.split_integer(32, 6)
    assert res1 == sorted(res1)
    assert res2 == sorted(res2)


def test_sum_of_parts_equals_value() -> None:
    """Перевірка, що сума елементів дорівнює початковому числу."""
    assert sum(app.split_integer.split_integer(17, 4)) == 17
    assert sum(app.split_integer.split_integer(32, 6)) == 32


def test_number_of_parts_is_correct() -> None:
    """Перевірка точної кількості частин у результаті."""
    assert len(app.split_integer.split_integer(32, 6)) == 6
    assert len(app.split_integer.split_integer(17, 4)) == 4


def test_value_smaller_than_number_of_parts() -> None:
    """Перевірка випадку, коли число менше за кількість частин."""
    assert app.split_integer.split_integer(3, 5) == [0, 0, 1, 1, 1]
    assert app.split_integer.split_integer(1, 3) == [0, 0, 1]
