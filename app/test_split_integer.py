from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    for value, parts in [(8, 1), (6, 2), (17, 4), (32, 6)]:
        assert sum(split_integer(value, parts)) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    for value, parts in [(6, 2), (8, 4), (10, 5)]:
        assert all(
            x == split_integer(value, parts)[0]
            for x in split_integer(value, parts)
        )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    for value in [1, 5, 10, 100]:
        assert split_integer(value, 1) == [value]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    for value, parts in [(17, 4), (32, 6), (10, 3)]:
        assert (split_integer(value, parts)
                == sorted(split_integer(value, parts)))


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    for value, parts in [(1, 2), (2, 3), (3, 5)]:
        assert (split_integer(value, parts)
                == [0] * (parts - value) + [1] * value)
