def split_integer(value: int, number_of_parts: int):
    """
    Разбивает число value на number_of_parts равных или почти равных частей.
    """
    base_value = value // number_of_parts
    remainder = value % number_of_parts

    # Создаем список с базовым значением
    result_list = [base_value] * number_of_parts

    # Распределяем остаток в порядке добавления элементов
    for i in range(remainder):
        result_list[i] += 1

    return result_list