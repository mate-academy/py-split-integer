from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 32
    number_of_parts = 6

    assert value == sum(split_integer(value, number_of_parts))


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 17
    number_of_parts = 4

    func = split_integer(value, number_of_parts)

    assert len(func) == number_of_parts


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 32
    number_of_parts = 6

    func = split_integer(value, number_of_parts)

    for part in range(len(func) - 1):
        assert abs(func[part] - func[part + 1]) <= 1


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 32
    number_of_parts = 6
    func = split_integer(value, number_of_parts)

    assert sorted(func) == func


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 0
    number_of_parts = 3

    func = split_integer(value, number_of_parts)

    assert func[0] == 0
