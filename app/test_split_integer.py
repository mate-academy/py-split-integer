from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    for value, number_of_parts in [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
    ]:
        result = split_integer(value, number_of_parts)

        assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    for value, number_of_parts in [
        (6, 2),
        (8, 4),
    ]:
        result = split_integer(value, number_of_parts)

        assert result == [value // number_of_parts] * number_of_parts


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    for value, number_of_parts in [
        (17, 4),
        (32, 6),
    ]:
        result = split_integer(value, number_of_parts)

        assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(1, 2)

    assert len(result) == 2
    assert sum(result) == 1
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
