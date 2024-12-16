from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    # Перевірка, чи сума частин дорівнює значенню
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(32, 6)) == 32


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    # Перевірка випадку, коли значення можна рівно поділити на частини
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(10, 5) == [2, 2, 2, 2, 2]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    # Перевірка випадку, коли значення ділиться на одну частину
    assert split_integer(8, 1) == [8]
    assert split_integer(100, 1) == [100]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    # Перевірка, чи частини відсортовані за зростанням
    result = split_integer(17, 4)
    assert result == [4, 4, 4, 5]
    assert result == sorted(result)  # Перевіряємо, чи відсортовані частини


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    # Тест на додавання нулів
    result = split_integer(3, 5)
    assert result == [0, 0, 0, 0, 3]
