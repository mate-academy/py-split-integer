from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 10
    parts = 3
    result = split_integer(value, parts)
    assert sum(result) == value, "Сумма частей должна быть равна value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 12
    parts = 4
    result = split_integer(value, parts)
    assert result == [3, 3, 3, 3],\
        "Не делит значение на равные части, если оно делится без остатка"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    parts = 1
    result = split_integer(value, parts)
    assert result == [8],\
        "Должен возвращать единственную часть, равную value, если parts=1"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    parts = 4
    result = split_integer(value, parts)
    assert result == sorted(result),\
        "Части должны быть отсортированы по возрастанию"
    assert max(result) - min(result) <= 1,\
        "Разница между максимальным и минимальным элементами должна быть ≤ 1"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 3
    parts = 5
    result = split_integer(value, parts)
    assert result == [0, 0, 1, 1, 1],\
        "Должен добавлять нули, если value < parts"
