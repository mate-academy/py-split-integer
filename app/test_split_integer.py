from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(20, 5)) == 20


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert len(set(split_integer(20, 4))) == 1


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(412, 1) == [412]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    list_test = split_integer(17, 4)

    for i in range(len(list_test) - 1):
        assert list_test[i] <= list_test[i + 1]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(3, 10)
    assert result == [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
