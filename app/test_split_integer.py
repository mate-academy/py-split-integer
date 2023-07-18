from .split_integer import split_integer


def test_difference_between_max_and_min() -> None:
    num_parts = 5
    for value in [10, 15, 20, 25, 30]:
        result = split_integer(value, num_parts)
        assert max(result) - min(result) <= 1


def test_array_sorted_ascending() -> None:
    num_parts = 5
    for value in [12, 18, 22, 29, 33]:
        result = split_integer(value, num_parts)
        assert result == sorted(result)


def test_single_element_array() -> None:
    assert split_integer(8, 1) == [8]


def test_two_elements_array() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_four_elements_array() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_six_elements_array() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
