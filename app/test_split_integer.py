import app.split_integer as m


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(m.split_integer(17, 4)) == 17
    assert sum(m.split_integer(32, 6)) == 32


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert m.split_integer(6, 2) == [3, 3]
    assert m.split_integer(15, 3) == [5, 5, 5]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert m.split_integer(8, 1) == [8]
    assert m.split_integer(42, 1) == [42]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert m.split_integer(17, 4) == [4, 4, 4, 5]
    assert m.split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert m.split_integer(2, 5) == [0, 0, 0, 1, 1]
    assert m.split_integer(3, 4) == [0, 1, 1, 1]


def test_should_return_exactly_number_of_parts_elements() -> None:
    assert len(m.split_integer(17, 4)) == 4
    assert len(m.split_integer(32, 6)) == 6
    assert len(m.split_integer(8, 1)) == 1


def test_difference_between_max_and_min_should_be_not_greater_than() -> None:
    assert max(m.split_integer(17, 4)) - min(m.split_integer(17, 4)) <= 1
    assert max(m.split_integer(32, 6)) - min(m.split_integer(32, 6)) <= 1
    assert max(m.split_integer(6, 2)) - min(m.split_integer(6, 2)) <= 1


def test_should_contain_only_integers() -> None:
    assert all(isinstance(x, int) for x in m.split_integer(17, 4))
    assert all(isinstance(x, int) for x in m.split_integer(32, 6))


def test_should_return_list() -> None:
    assert isinstance(m.split_integer(17, 4), list)
