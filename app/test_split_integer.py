import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize("value, number_of_parts, expected_result", [
    (8, 1, [8]),
    (6, 2, [3, 3]),
    (17, 4, [4, 4, 4, 5]),
    (32, 6, [5, 5, 5, 5, 6, 6]),

    (4, 4, [1, 1, 1, 1]),
    (1, 4, [0, 0, 0, 1]),
    (0, 5, [0, 0, 0, 0, 0]),
    (7, 5, [1, 1, 1, 2, 2]),
])
def test_split_integer_with_correct_result_and_properties(
    value: int,
    number_of_parts: int,
    expected_result: list[int]
) -> None:
    """
    Проверяет, что функция возвращает правильный, отсортированный массив,
    и что сумма частей равна value.
    """
    actual = split_integer(value, number_of_parts)

    assert actual == expected_result, (
        f"Для ({value}, {number_of_parts}) ожидалось {expected_result}, "
        f"получено {actual}"
    )

    # 2. Проверка, что сумма всех частей равна исходному value
    assert sum(actual) == value, (
        f"Сумма частей ({sum(actual)}) не равна исходному значению ({value})"
    )

    # 3. Проверка основного требования: max(array) - min(array) <= 1
    if number_of_parts > 0 and actual:
        assert max(actual) - min(actual) <= 1, (
            f"Разница max/min больше 1: {max(actual)} - {min(actual)}"
        )
