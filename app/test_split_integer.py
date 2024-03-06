from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(8, 3)) == 8
    assert sum(split_integer(15, 5)) == 15
    assert sum(split_integer(20, 4)) == 20


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(10, 2) == [5, 5]
    assert split_integer(12, 3) == [4, 4, 4]
    assert split_integer(30, 6) == [5, 5, 5, 5, 5, 5]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(20, 1) == [20]
    assert split_integer(30, 1) == [30]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    results = split_integer(15, 4)
    assert sorted(results) == results

    results = split_integer(25, 5)
    assert sorted(results) == results

    results = split_integer(35, 6)
    assert sorted(results) == results


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    results = split_integer(3, 5)
    assert sorted(results) == results

    results = split_integer(5, 7)
    assert sorted(results) == results

    results = split_integer(10, 15)
    assert sorted(results) == results
