from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(8, 1)) == 8,\
        "Sum of the parts should be equal to the original value."


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(8, 4) == [2, 2, 2, 2],\
        "Value should be split into equal parts when divisible."
    assert split_integer(10, 5) == [2, 2, 2, 2, 2],\
        "Value should be split into equal parts when divisible."


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8],\
        ("When splitting into one part,"
         " the result should equal the original value.")
    assert split_integer(15, 1) == [15],\
        ("When splitting into one part,"
         " the result should equal the original value.")


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (split_integer(17, 4)
            == sorted(split_integer(17, 4)) == [4, 4, 4, 5]), \
        "Parts should be sorted when they are not equal."
    assert (split_integer(32, 6)
            == sorted(split_integer(32, 6)) == [5, 5, 5, 5, 6, 6]), \
        "Parts should be sorted when they are not equal."


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1], \
        ("When value is less than the number of parts,"
         " the result should include zeros.")
