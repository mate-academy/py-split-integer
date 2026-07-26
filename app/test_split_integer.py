from app.split_integer import split_integer


def test_length_of_result_should_be_equal_to_number_of_parts() -> None:
    result = split_integer(17, 4)
    assert len(result) == 4


def test_all_elements_should_be_integers() -> None:
    result = split_integer(17, 4)
    assert all(isinstance(x, int) for x in result)


def test_max_minus_min_should_be_less_or_equal_one() -> None:
    result = split_integer(17, 4)
    assert max(result) - min(result) <= 1


def test_split_integer_example_32_6() -> None:
    result = split_integer(32, 6)
    assert result == [5, 5, 5, 5, 6, 6]


def test_result_should_be_sorted_by_default() -> None:
    result = split_integer(32, 6)
    assert result == sorted(result)
