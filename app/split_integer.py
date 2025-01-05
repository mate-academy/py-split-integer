# Код split_integer.py (папка app)
def split_integer(value: int, number_of_parts: int) -> list:
    # Если только одна часть, вернуть значение как единственную часть
    if number_of_parts == 1:
        return [value]

    # Если значение меньше количества частей, заполняем нулями
    if value < number_of_parts:
        parts = [0] * (number_of_parts - 1) + [value]
    else:
        # Базовый размер части
        part_size = value // number_of_parts
        # Остаток, который нужно распределить
        remainder = value % number_of_parts

        # Инициализируем части базовым размером
        parts = [part_size] * number_of_parts

        # Распределяем остаток равномерно
        for i in range(remainder):
            parts[i] += 1

    # Возвращаем отсортированный результат
    return sorted(parts)