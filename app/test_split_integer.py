from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
            ), "Sum of the parts should be equal to 32"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (split_integer(30, 5) == [6, 6, 6, 6, 6]
            ), ("Test should split into equal "
                "parts when value divisible by parts")


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (split_integer(53, 1) == [53]
            ), ("Test should return part equals "
                "to value when split into one part")


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (split_integer(93, 6) == [
        15, 15, 15, 16, 16, 16]), (
        "Test parts should be sorted when they are not equal")


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (split_integer(3, 9) > [0]
            ), "Test should add zeros when value less than number of parts"
