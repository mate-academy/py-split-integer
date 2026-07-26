from app.split_integer import split_integer


def test_sum_or_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17


def test_split_integer_should_split_into_equal_parts() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_parts_should_be_sorted_ascending() -> None:
    result = split_integer(32, 6)
    assert result == sorted(result)


def test_difference_between_max_and_min_should_be_less_than_two() -> None:
    result = split_integer(18, 4)
    assert max(result) - min(result) <= 1


def test_should_return_part_equals_to_value_with_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_result_should_have_correct_number_of_parts() -> None:
    number_of_parts = 6
    assert len(split_integer(32, number_of_parts)) == number_of_parts


def test_remainder_should_be_distributed_evenly() -> None:
    """
    Este test es crítico para detectar si el residuo se acumula erróneamente.
    Para (20, 6):
    20 // 6 = 3 (base)
    20 % 6 = 2 (residuo) -> Estos 2 deben repartirse al final.
    Resultado esperado: [3, 3, 3, 3, 4, 4]
    """
    assert split_integer(20, 6) == [3, 3, 3, 3, 4, 4]
