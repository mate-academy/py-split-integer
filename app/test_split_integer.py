from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    input_data = (32, 6)
    test_res = split_integer(input_data[0], input_data[1])
    assert sum(test_res) == input_data[0]


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    input_data = (36, 6)
    test_res = split_integer(input_data[0], input_data[1])
    assert input_data[0] // input_data[1] == len(test_res)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    input_data = (36, 1)
    test_res = split_integer(input_data[0], input_data[1])
    assert len(test_res) == 1


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    input_data = (32, 6)
    test_res = split_integer(input_data[0], input_data[1])
    assert test_res == sorted(test_res)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    input_data = (1, 6)
    test_res = split_integer(input_data[0], input_data[1])
    assert test_res.count(0) == input_data[1] - input_data[0]
