from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(45, 7)) == 45


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    check_list = split_integer(49, 7)
    assert all(elem == check_list[0] for elem in check_list)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    check_list = split_integer(65, 6)
    assert all(
        check_list[i] <= check_list[i + 1]
        for i in range(len(check_list) - 1)
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(5, 7).count(0) > 0
