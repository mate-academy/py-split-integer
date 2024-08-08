from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    error_mes = "Sum of the parts should be equal to `value`"
    assert sum(split_integer(17, 4)) == 17, error_mes


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    error_mes = (
        "'value' should split into equal parts"
        " when value divisible by parts"
    )
    assert split_integer(6, 2) == [3, 3], error_mes


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    error_mes = "Should return part equals to value when split into one part"
    assert split_integer(8, 1) == [8], error_mes


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    error_mes = "Parts should be sorted when they are not equal"
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6], error_mes


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    error_mes = "Should add zeros when value is less than number of parts"
    assert split_integer(2, 3) == [0, 1, 1], error_mes
