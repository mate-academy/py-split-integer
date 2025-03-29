from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(52, 6)) == 52, \
        "Sum of parts should be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (split_integer(8, 2) == [4, 4]), \
        (f"Array should split value 8 on two equal parts not "
         f"{split_integer(8, 2)}")


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (split_integer(9, 1) == [9]), \
        "When number of parts equal to 1, one part should be equal to value 9"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (split_integer(32, 6) == [5, 5, 5, 5, 6, 6]), \
        "Parts should be sorted in ascending order"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (split_integer(3, 5) == [0, 0, 1, 1, 1]), \
        ("Array from value 3 and number of parts 5 should be equal "
         "[0, 0, 1, 1, 1]")
