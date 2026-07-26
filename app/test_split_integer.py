from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 6
    res = split_integer(value, 2)
    assert sum(res) == value, f"Expected sum {value}, got {sum(res)}"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 30
    number_of_parts = 6
    res = split_integer(value, number_of_parts)
    assert len(res) == number_of_parts, \
        f"Expected {number_of_parts} parts, got {len(res)}"
    assert all(part == res[0] for part in res), \
        "Expected all parts to be equal"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 6
    res = split_integer(value, 1)
    assert res == [value], f"Expected [{value}], got {res}"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 32
    number_of_parts = 6
    res = split_integer(value, number_of_parts)
    assert res == sorted(res), f"Expected sorted parts, got {res}"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 5
    number_of_parts = 6
    res = split_integer(value, number_of_parts)
    assert len(res) == number_of_parts, \
        f"Expected {number_of_parts} parts, got {len(res)}"
    assert res.count(0) == number_of_parts - value, \
        "Expected correct number of zeros"
