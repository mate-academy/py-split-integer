from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(6, 2)) == 6
    assert sum(split_integer(32, 6)) == 32
    assert sum(split_integer(3, 5)) == 3
    assert sum(split_integer(0, 5)) == 0
    assert sum(split_integer(1, 1)) == 1
    assert sum(split_integer(100, 9)) == 100
    assert sum(split_integer(10, 3)) == 10


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert len(set(split_integer(6, 2))) == 1

    assert split_integer(12, 4) == [3, 3, 3, 3]
    assert len(set(split_integer(12, 4))) == 1

    assert split_integer(20, 5) == [4, 4, 4, 4, 4]
    assert len(set(split_integer(20, 5))) == 1

    assert len(set(split_integer(100, 10))) == 1


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(1, 1) == [1]
    assert split_integer(100, 1) == [100]


def test_parts_should_be_sorted_ascending() -> None:
    assert split_integer(17, 4) == sorted(split_integer(17, 4))
    assert split_integer(32, 6) == sorted(split_integer(32, 6))
    assert split_integer(10, 3) == sorted(split_integer(10, 3))


def test_difference_between_max_and_min_should_be_at_most_one() -> None:
    test_cases = [(17, 4), (32, 6), (3, 5), (100, 9), (0, 5), (1, 3), (10, 3)]
    for value, parts in test_cases:
        result = split_integer(value, parts)
        if result:
            assert max(result) - min(result) <= 1


def test_correct_number_of_parts_returned() -> None:
    assert len(split_integer(17, 4)) == 4
    assert len(split_integer(32, 6)) == 6
    assert len(split_integer(10, 3)) == 3
    assert len(split_integer(8, 1)) == 1


def test_split_10_into_3_parts() -> None:
    assert split_integer(10, 3) == [3, 3, 4]


def test_split_11_into_3_parts() -> None:
    assert split_integer(11, 3) == [3, 4, 4]


def test_split_17_into_4_parts() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_split_32_into_6_parts() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_split_3_into_5_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_count_of_larger_elements_equals_remainder() -> None:
    assert split_integer(10, 3).count(4) == 1
    assert split_integer(10, 3).count(3) == 2

    assert split_integer(11, 3).count(4) == 2
    assert split_integer(11, 3).count(3) == 1

    assert split_integer(17, 4).count(5) == 1
    assert split_integer(17, 4).count(4) == 3

    assert split_integer(32, 6).count(6) == 2
    assert split_integer(32, 6).count(5) == 4


def test_examples_from_specification() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_all_elements_are_integers() -> None:
    assert all(isinstance(x, int) for x in split_integer(17, 4))
    assert all(isinstance(x, int) for x in split_integer(32, 6))
    assert all(isinstance(x, int) for x in split_integer(3, 5))
    assert all(isinstance(x, int) for x in split_integer(0, 5))
