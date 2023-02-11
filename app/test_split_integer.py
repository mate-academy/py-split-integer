from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    arguments = [[8, 1], [6, 2], [17, 4], [32, 6], [8, 8], [3, 6], [1, 1]]
    for arg in arguments:
        actual = split_integer(arg[0], arg[1])
        assert len(actual) == arg[1]
        assert sum(actual) == arg[0]


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    arguments = [[9, 3], [6, 2], [16, 4], [48, 6], [8, 1], [1, 1], [10, 10], [0, 5]]
    for arg in arguments:
        actual = split_integer(arg[0], arg[1])
        assert len(actual) == arg[1]
        for item in actual:
            assert item == arg[0]/arg[1]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    arguments = [[9, 1], [6, 1], [16, 1], [48, 1], [1, 1]]
    for arg in arguments:
        actual = split_integer(arg[0], arg[1])
        if arg[0] % arg[1] == 0:
            assert actual[0] == actual[-1]
        else:
            assert actual[0] == actual[-1] - 1
        assert len(actual) == arg[1]
        assert actual[0] == arg[0]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    arguments = [[9, 2], [6, 4], [16, 7], [48, 7], [8, 8], [18, 17], [17, 18]]
    for arg in arguments:
        actual = split_integer(arg[0], arg[1])
        assert len(actual) == arg[1]
        if arg[0] % arg[1] == 0:
            assert actual[0] == actual[-1]
        else:
            assert actual[0] == actual[-1] - 1
        assert actual == sorted(actual)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    arguments = [[3, 9], [1, 5], [6, 14], [4, 6], [1, 2]]
    for arg in arguments:
        actual = split_integer(arg[0], arg[1])
        assert len(actual) == arg[1]
        if arg[0] % arg[1] == 0:
            assert actual[0] == actual[-1]
        else:
            assert actual[0] == actual[-1] - 1
        for index in range(len(actual)):
            if index < arg[1] - arg[0]:
                assert actual[index] == 0
            else:
                assert actual[index] == 1
