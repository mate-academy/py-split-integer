from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    parts_of_int = split_integer(value=9, number_of_parts=3)
    assert (sum(parts_of_int) == 9)


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts_of_int = split_integer(value=16, number_of_parts=4)
    assert (parts_of_int[0] == parts_of_int[1]
            and parts_of_int[1] == parts_of_int[2]
            and parts_of_int[2] == parts_of_int[3])


def test_should_split_on_not_equal_parts_when_value_is_not_divisible() -> None:
    assert (split_integer(value=16, number_of_parts=5) != [3, 3, 3, 3, 3])


def test_should_not_split_into_equal_nums_and_increment_the_last_one() -> None:
    assert (split_integer(32, 6) != [5, 5, 5, 5, 5, 6])


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (split_integer(value=7, number_of_parts=1)[0] == 7)


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts_of_int = split_integer(value=16, number_of_parts=5)
    assert (parts_of_int == sorted(parts_of_int))


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    parts_of_int = split_integer(value=1, number_of_parts=3)
    assert (parts_of_int[0] == 0 and parts_of_int[1] == 0)
