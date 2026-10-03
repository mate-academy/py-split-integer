from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (
        sum(split_integer(32, 6)) == 32
    ), "Sum of the parts should be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert (
        split_integer(16, 4) == [4, 4, 4, 4]
    ), "Should split into equal parts when value divisible by parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(32, 1) == [32]
    ), "Should return part equals to value when split into one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(17, 4) == [4, 4, 4, 5]
    ), "Parts should be sorted when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(1, 4) == [0, 0, 0, 1]
    ), "Should add zeros when value is less than number of parts"


def test_min_and_max_should_have_difference_of_only_one() -> None:
    assert (
        abs(
            min(
                split_integer(17, 4)
            )
            - max(
                split_integer(17, 4)
            )
        ) <= 1
    ), "Min and max should have difference of only one"


def test_result_should_contain_exactly_number_of_parts_elements() -> None:
    assert (
        len(split_integer(54, 6)) == 6
    ), "Result should contain exactly number of parts elements"
