from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    ls = {
        "value": 8,
        "number_of_parts": 1,
        "result": [8]
    }
    actual = split_integer(ls["value"], ls["number_of_parts"])
    assert actual == ls["result"]


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    ls = {
        "value": 6,
        "number_of_parts": 2,
        "result": [3, 3]
    }
    actual = split_integer(ls["value"], ls["number_of_parts"])
    assert actual == ls["result"]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    ls = {
        "value": 17,
        "number_of_parts": 4,
        "result": [4, 4, 4, 5]
    }
    actual = split_integer(ls["value"], ls["number_of_parts"])
    assert actual == ls["result"]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    ls = {
        "value": 32,
        "number_of_parts": 6,
        "result": [5, 5, 5, 5, 6, 6]
    }
    actual = split_integer(ls["value"], ls["number_of_parts"])
    assert actual == ls["result"]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    ls = {
        "value": 2,
        "number_of_parts": 4,
        "result": [0, 0, 1, 1]
    }
    actual = split_integer(ls["value"], ls["number_of_parts"])
    assert actual == ls["result"]
