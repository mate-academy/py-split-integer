from app.split_integer import split_integer
def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert sum(result) == value  # Сумма частей должна быть равна value

def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 10
    number_of_parts = 5
    result = split_integer(value, number_of_parts)
    assert result == [2, 2, 2, 2, 2]  # Равное разделение

def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1
    result = split_integer(value, number_of_parts)
    assert result == [8]  # Одна часть равна значению

def test_parts_should_distribute_remainder_correctly() -> None:
    value = 10
    number_of_parts = 3
    result = split_integer(value, number_of_parts)
    assert result == [4, 3, 3]  # Остаток распределен корректно

def test_should_handle_value_less_than_parts() -> None:
    value = 3
    number_of_parts = 5
    result = split_integer(value, number_of_parts)
    assert result == [1, 1, 1, 0, 0]  # Равномерное распределение при value < number_of_parts

def test_should_handle_large_numbers() -> None:
    value = 100000
    number_of_parts = 7
    result = split_integer(value, number_of_parts)
    assert sum(result) == value  # Сумма равна исходному значению
    assert max(result) - min(result) <= 1  # Разница между элементами максимум 1

def test_no_sorting_of_parts() -> None:
    value = 13
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert result == [4, 3, 3, 3]