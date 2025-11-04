from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    number_of_parts = 4
    subject = split_integer(value, number_of_parts)

    assert sum(subject) == value
    assert max(subject) - min(subject) <= 1


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    number_of_parts = 2
    subject = split_integer(value, number_of_parts)
    expected = [3, 3]

    assert subject == expected
    assert len(subject) == number_of_parts
    assert sum(subject) == value


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1
    subject = split_integer(value, number_of_parts)

    assert len(subject) == number_of_parts
    assert subject == value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 32
    number_of_parts = 6
    subject = split_integer(value, number_of_parts)
    expected = [5, 5, 5, 5, 6, 6]

    assert sorted(subject) == expected


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 1
    number_of_parts = 3
    subject = split_integer(value, number_of_parts)

    assert len(subject) == number_of_parts
