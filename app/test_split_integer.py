from app.split_integer import split_integer


def test_split_on_equal_parts() -> None:
    assert split_integer(10, 5) == [2, 2, 2, 2, 2]
    assert split_integer(9, 3) == [3, 3, 3]


def test_sum_of_parts_equals_value() -> None:
    for value in range(1, 20):
        for parts in range(1, value + 1):
            assert sum(split_integer(value, parts)) == value


def test_difference_between_parts_not_more_than_one() -> None:
    for value in range(1, 50):
        for parts in range(1, value + 1):
            result = split_integer(value, parts)
            assert max(result) - min(result) <= 1


def test_correct_number_of_parts() -> None:
    assert len(split_integer(10, 5)) == 5
    assert len(split_integer(7, 2)) == 2


def test_distribution_of_remainder() -> None:
    assert split_integer(10, 3) == [3, 3, 4]
    assert split_integer(11, 3) == [3, 4, 4]


def test_one_part_equals_value() -> None:
    assert split_integer(10, 1) == [10]


def test_each_part_positive_if_value_positive() -> None:
    for i in range(1, 10):
        assert all(x > 0 for x in split_integer(i * 3, 3))


def test_large_numbers() -> None:
    result = split_integer(10**6, 7)
    assert sum(result) == 10**6
    assert max(result) - min(result) <= 1
