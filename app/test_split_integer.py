from app.split_integer import split_integer


def test_split_integer_result_length_equals_number_of_parts():
    assert len(split_integer(17, 4)) == 4


def test_split_integer_result_sum_equals_value():
    assert sum(split_integer(17, 4)) == 17


def test_split_integer_parts_differ_by_at_most_one():
    result = split_integer(32, 6)
    assert max(result) - min(result) <= 1


def test_split_integer_result_is_sorted_ascending():
    result = split_integer(32, 6)
    assert result == sorted(result)


def test_split_integer_returns_single_element_list_when_parts_is_one():
    assert split_integer(8, 1) == [8]


def test_split_integer_returns_equal_parts_when_perfectly_divisible():
    assert split_integer(6, 2) == [3, 3]


def test_split_integer_handles_value_less_than_number_of_parts():
    result = split_integer(2, 5)
    # Verifica as propriedades fundamentais mesmo quando há zeros
    assert len(result) == 5
    assert sum(result) == 2
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
