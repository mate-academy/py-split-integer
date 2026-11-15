from random import randint


from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value_parameter = randint(20, 100)
    parts_parameter = randint(1, 10)
    assert (
        sum(split_integer(value_parameter,
                          parts_parameter)) == value_parameter
    ), (f"The Sum of the {parts_parameter} into which {value_parameter} is"
        f" split shall be equal to {value_parameter}!")


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts_parameter = randint(2, 10)
    value_multiplier = randint(2, 10)
    for number in split_integer(value_multiplier * parts_parameter,
                                parts_parameter):
        assert (
            number == value_multiplier
        ), (f"Since the value {value_multiplier * parts_parameter} is a "
            f"multiple of {parts_parameter}, the function must always return "
            f"{value_multiplier}, and not {number}!")


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value_parameter = randint(20, 100)
    assert (
        split_integer(value_parameter,
                      1)[0] == value_parameter
    ), (f"Splitting {value_parameter} into one part shall return "
        f"{value_parameter}, and not {split_integer(value_parameter, 1)[0]}!")


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value_parameter = randint(20, 100)
    parts_parameter = randint(1, 10)
    result_list = split_integer(value_parameter, parts_parameter)
    assert (
        result_list == sorted(result_list)
        and len(result_list) == parts_parameter
        and result_list[-1] - result_list[0] <= 1
    ), "Split integer shall return a sorted list!"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    number_of_parts = randint(20, 100)
    number_of_zeros = randint(1, 19)
    result_list = split_integer(number_of_parts - number_of_zeros,
                                number_of_parts)
    number_of_zeros_split = 0
    for result_value in result_list:
        if result_value == 0:
            number_of_zeros_split += 1
    assert (
        number_of_zeros == number_of_zeros_split
    ), (f"To split the value {number_of_parts - number_of_zeros} into "
        f"{number_of_parts} parts , the function must return "
        f"{number_of_zeros} zeros, not {number_of_zeros_split}!")
