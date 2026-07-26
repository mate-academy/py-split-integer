from app.split_integer import split_integer


# тестовая сумма частей должна быть равна значению
def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(8, 2)) == 8


# тест должен быть разделен на равные части, когда значение делится на части
def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(20, 5) == [4, 4, 4, 4, 4]


# тест должен возвращать часть, равную значению, при разделении на одну часть
def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


# тестовые части должны быть отсортированы, если они не равны
def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


# тест должен добавлять нули, когда значение меньше количества частей
def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(6, 8) == [0, 0, 1, 1, 1, 1, 1, 1]
