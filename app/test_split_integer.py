from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(21, 3)) == 21, (
        "Sum of the parts should be equal to value!"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(6, 2)
    assert all(split_integer(6, 2)[i - 1] == result[i]
               for i in range(1, len(split_integer(6, 2)))), (
        "Should split into equal parts when value divisible by parts!"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(11, 1)[0] == 11, (
        "Should return part equals to value when split into one part!"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(45, 2) == sorted(split_integer(45, 2)), (
        "Parts should be sorted when they are not equal!"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 4) == [0, 1, 1, 1], (
        "Should add zeros when value is less than the number of parts!"
    )
