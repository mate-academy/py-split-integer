# split_integer.py

def split_integer(value: int, parts: int) -> list:
    # Підрахунок базової частини і залишку
    quotient, remainder = divmod(value, parts)

    # Створення списку, де кожен елемент - це основний поділ
    result = [quotient] * parts

    # Розподіл залишку на перші елементи
    for i in range(remainder):
        result[i] += 1

    # Сортуємо результат у порядку зростання
    result.sort()

    return result
