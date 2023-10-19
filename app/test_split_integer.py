from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert (sum(split_integer(6, 3)) == 6), (
        "Sum of the parts should be equal to value!"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    func = split_integer(12, 6)
    assert all(func[i - 1] == func[i] for i in range(1, len(func))), (
        "Should split into equal parts when value divisible by parts"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(17, 1)[0]
    assert result == 17, (
        "should return part equals to values when split into one part"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(32, 6)
    assert result == sorted(result), (
        "parts should be sorted"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(2, 3)
    assert result == [0, 1, 1], (
        "add zeros when value less than parts"
    )
