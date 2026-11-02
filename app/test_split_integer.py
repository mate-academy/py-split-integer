import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (5, 5, [1, 1, 1, 1, 1]),
        (10, 3, [3, 3, 4]),
    ],
)
def test_split_integer_expected_results(value, number_of_parts, expected):
    """Testa se a função retorna exatamente os valores esperados para casos específicos."""
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (10, 1),
        (15, 3),
        (22, 5),
        (100, 13),
        (7, 4),
    ],
)
def test_split_integer_properties(value, number_of_parts):
    """Testa se o resultado atende a todas as restrições matemáticas da função."""
    result = split_integer(value, number_of_parts)

    # 1. Verifica se o tamanho do array corresponde ao número de partes
    assert len(result) == number_of_parts

    # 2. Verifica se a soma dos elementos resulta no valor original
    assert sum(result) == value

    # 3. Verifica se o array está ordenado em ordem crescente
    assert result == sorted(result)

    # 4. Verifica se a diferença entre o elemento máximo e mínimo é <= 1
    if result:
        assert max(result) - min(result) <= 1
