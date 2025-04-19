def split_integer(value: int, number_of_parts: int) -> list:
    # Базове значення кожної частини
    base_value = value // number_of_parts
    # Залишок від ділення
    remainder = value % number_of_parts

    # Створення списку з базовими значеннями
    result = [base_value] * number_of_parts

    # Додаємо залишок до останніх частин
    for i in range(remainder):
        result[number_of_parts - 1 - i] += 1

    # Повертаємо відсортований список
    return sorted(result)
