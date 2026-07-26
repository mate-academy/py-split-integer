from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    # Teste se a soma das partes é igual ao valor original
    value = 17
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    # Teste quando o valor é divisível pelo número de partes
    value = 6
    number_of_parts = 2
    result = split_integer(value, number_of_parts)
    assert result == [3, 3]
    assert all(x == result[0] for x in result)  # Todos os elementos são iguais


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    # Teste quando há apenas uma parte
    value = 8
    number_of_parts = 1
    result = split_integer(value, number_of_parts)
    assert result == [value]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    # Teste se as partes estão ordenadas quando não são iguais
    value = 17
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert result == sorted(result)  # Verifica se está ordenado
    assert result == [4, 4, 4, 5]  # Exemplo específico


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    # Teste quando o valor é menor que o número de partes
    value = 3
    number_of_parts = 5
    result = split_integer(value, number_of_parts)
    assert sum(result) == value
    assert len(result) == number_of_parts
    # Verifica se a diferença entre máximo e mínimo é <= 1
    assert max(result) - min(result) <= 1
    # Verifica se há zeros no resultado
    assert 0 in result
