from app.split_integer import split_integer


def test_single_part() -> None:
    """Проверка, если нужно всего 1 часть."""
    result = split_integer(8, 1)
    assert result == [8], f"Expected [8], got {result}"


def test_equal_parts() -> None:
    """Проверка, если value делится на части без остатка."""
    result = split_integer(6, 2)
    assert result == [3, 3], f"Expected [3, 3], got {result}"


def test_unequal_parts() -> None:
    """Проверка, если value не делится на части без остатка."""
    result = split_integer(17, 4)
    assert result == [4, 4, 4, 5], f"Expected [4, 4, 4, 5], got {result}"


def test_sorted_output() -> None:
    """Проверка, что результат всегда отсортирован."""
    result = split_integer(25, 5)
    assert result == sorted(result), f"Result is not sorted: {result}"


def test_max_min_difference() -> None:
    """Проверка, что разница между max и min ≤ 1."""
    result = split_integer(10, 3)
    max_min_diff = max(result) - min(result)
    assert max_min_diff <= 1, f"Max-min difference is too large: {result}"


def test_sum_equals_value() -> None:
    """Проверка, что сумма элементов равна value."""
    result = split_integer(18, 4)
    assert sum(result) == 18, f"Sum mismatch: {result}"


def test_exact_number_of_parts() -> None:
    """Проверка, что результат содержит ровно number_of_parts элементов."""
    result = split_integer(32, 6)
    assert len(result) == 6, f"Expected 6 parts, got {len(result)}: {result}"


def test_large_value_and_parts() -> None:
    """Проверка с большими числами."""
    result = split_integer(1000, 100)
    assert len(result) == 100, f"Expected 100 parts, got {len(result)}"
    assert sum(result) == 1000, f"Sum mismatch: {result}"
    max_min_diff = max(result) - min(result)
    assert max_min_diff <= 1, f"Max-min difference is too large: {result}"


def test_edge_case_small_value() -> None:
    """Проверка с минимальным значением."""
    result = split_integer(1, 1)
    assert result == [1], f"Expected [1], got {result}"
