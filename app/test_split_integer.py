import pytest
from app.split_integer import split_integer


# 🔹 1. Testes dos exemplos oficiais do enunciado
@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
    ],
)
def test_should_match_examples_from_specification(
    value: int,
    number_of_parts: int,
    expected: list[int],
) -> None:
    """
    Testa se os exemplos oficiais do enunciado retornam exatamente o resultado esperado.
    """
    assert split_integer(value, number_of_parts) == expected


# 🔹 2. Testes gerais para validar propriedades obrigatórias
@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (10, 3),
        (3, 5),
        (20, 4),
        (21, 4),
    ],
)
def test_general_behavior_of_split_integer(
    value: int,
    number_of_parts: int,
) -> None:
    """
    Testa propriedades gerais obrigatórias:
    - soma total = valor original
    - quantidade de partes correta
    - todos inteiros
    - lista ordenada
    - diferença entre maior e menor <= 1
    """
    result = split_integer(value, number_of_parts)

    # Soma total igual ao valor original
    assert sum(result) == value

    # Quantidade de partes correta
    assert len(result) == number_of_parts

    # Todos os elementos devem ser inteiros
    assert all(isinstance(x, int) for x in result)

    # Lista deve estar ordenada
    assert result == sorted(result)

    # Diferença máxima entre o maior e o menor valor <= 1
    assert max(result) - min(result) <= 1
