from app.split_integer import split_integer


def test_length_should_be_equal_to_number_of_parts() -> None:
    assert len(split_integer(17, 4)) == 4


def test_sum_of_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17


def test_difference_between_max_and_min_less_or_equal_one() -> None:
    result = split_integer(17, 4)
    assert max(result) - min(result) <= 1


def test_parts_should_be_sorted_ascending() -> None:
    result = split_integer(32, 6)
    assert result == sorted(result)


def test_should_return_list_with_value_when_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_equal_when_value_divisible() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_greater_parts_should_be_at_the_end_when_not_divisible() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_should_add_zeros_when_value_less_than_number_of_parts() -> None:
    assert split_integer(2, 4) == [0, 0, 1, 1]


def test_should_split_when_remainder_is_one() -> None:
    assert split_integer(7, 3) == [2, 2, 3]


def test_should_split_when_remainder_is_two() -> None:
    assert split_integer(8, 3) == [2, 3, 3]


def test_should_split_when_remainder_is_three() -> None:
    assert split_integer(11, 4) == [2, 3, 3, 3]


def test_should_preserve_sum_for_other_values() -> None:
    result = split_integer(19, 6)
    assert sum(result) == 19


def test_should_keep_sorted_for_other_values() -> None:
    result = split_integer(19, 6)
    assert result == sorted(result)


def test_neighbor_difference_should_not_exceed_one() -> None:
    result = split_integer(19, 6)

    for left, right in zip(result, result[1:]):
        assert right - left <= 1
