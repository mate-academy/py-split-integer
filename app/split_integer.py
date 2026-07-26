def split_integer(value: int, number_of_parts: int) -> list:
    base_value = value // number_of_parts
    remainder = value % number_of_parts
    parts = [base_value] * number_of_parts

    for i in range(remainder):
        parts[i] += 1  # Розподіляємо залишок на перші елементи

    return sorted(parts)  # Гарантуємо, що список відсортований
