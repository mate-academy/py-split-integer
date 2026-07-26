from app.split_integer import split_integer


def test_should_split_into_equal_parts_when_divisible() -> None:
    assert split_integer(10, 5) == [2, 2, 2, 2, 2]


def test_should_split_17_into_4_parts() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_should_split_32_into_6_parts() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_split_8_into_1_part() -> None:
    assert split_integer(8, 1) == [8]


def test_should_split_6_into_2_parts() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_result_length_matches_number_of_parts() -> None:
    result = split_integer(25, 7)
    assert len(result) == 7


def test_sum_of_parts_equals_original_value() -> None:
    result = split_integer(19, 3)
    assert sum(result) == 19


def test_parts_are_sorted_in_non_decreasing_order() -> None:
    result = split_integer(50, 8)
    assert result == sorted(result)
