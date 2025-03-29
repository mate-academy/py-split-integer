from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(15, 4))
        == 15
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        all(
            part == split_integer(16, 4)[0]
            for part in split_integer(16, 4)
        )
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(16, number_of_parts=1)[0] == 16
    assert len(split_integer(16, 1)) == 1


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(17, 3)
        == sorted(split_integer(17, 3))
    )


def test_should_add_zeros_when_value_is_less_than_4() -> None:
    assert len(split_integer(5, 8)) == 8
    assert (
        split_integer(5, 8).count(0)
        == 8 - 5
    )
