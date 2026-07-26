from app.split_integer import split_integer


def test_should_return_values_with_difference_max_and_min_1_or_less() -> None:
    assert max(split_integer(32, 6)) - min(split_integer(32, 6)) <= 1


def test_list_len_should_be_equal_to_number_of_parts() -> None:
    assert len(split_integer(32, 6)) == 6


def test_should_return_exact_output_for_complex_examples() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(8, 3)) == 8


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert len(set(split_integer(15, 3))) == 1


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(7, 1) == [7]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(29, 7) == sorted(split_integer(29, 7))


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert 0 in split_integer(2, 3)
