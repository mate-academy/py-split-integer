from app.split_integer import split_integer


# sum of the parts should be equal to value
def test_check_sum_of_the_parts() -> None:
    expected_parts = split_integer(20, 4)
    assert sum(expected_parts) == 20


# should split into equal parts when value divisible by parts
def test_split_into_equal_parts() -> None:
    expected_parts = split_integer(30, 5)
    assert all(
        part == 30 // 5 for part in expected_parts)


# should return part equals to value when split into one part
def test_split_to_single_part() -> None:
    expected_parts = split_integer(8, 1)
    assert expected_parts == [8]


# parts should be sorted when they are not equal
def test_sort_non_equal_parts() -> None:
    expected_parts = split_integer(17, 4)
    sorted_parts = sorted(expected_parts)
    assert expected_parts == sorted_parts


# should add zeros when value is less than number of parts
def test_add_zeros_for_small_value() -> None:
    expected_parts = split_integer(3, 4)
    assert expected_parts == [0, 1, 1, 1]
