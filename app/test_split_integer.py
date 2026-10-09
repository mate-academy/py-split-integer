import app.split_integer


def test_sum_of_the_parts_is_equal_to_value() -> None:
    assert sum(app.split_integer.split_integer(17, 4)) == 17
    assert sum(app.split_integer.split_integer(32, 6)) == 32


def test_should_split_into_equal_parts() -> None:
    assert app.split_integer.split_integer(6, 2) == [3, 3]
    assert app.split_integer.split_integer(8, 1) == [8]


def test_should_split_with_remainder() -> None:
    assert app.split_integer.split_integer(17, 4) == [4, 4, 4, 5]
    assert app.split_integer.split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_return_ascending_sorted_list() -> None:
    result1 = app.split_integer.split_integer(17, 4)
    assert result1 == sorted(result1)

    result2 = app.split_integer.split_integer(32, 6)
    assert result2 == sorted(result2)


def test_difference_between_max_and_min_is_less_or_equal_to_1() -> None:
    result1 = app.split_integer.split_integer(17, 4)
    assert max(result1) - min(result1) <= 1

    result2 = app.split_integer.split_integer(32, 6)
    assert max(result2) - min(result2) <= 1


def test_split_integer_should_return_list_of_given_length() -> None:
    assert len(app.split_integer.split_integer(17, 4)) == 4
    assert len(app.split_integer.split_integer(32, 6)) == 6
