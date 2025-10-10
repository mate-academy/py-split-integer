from app.split_integer import split_integer

# Checks sum, length and even distribution of parts
def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    parts = split_integer(10, 6)
    assert sum(parts) == 10, "Sum of the parts should be equal to value"
    assert len(parts) == 6
    assert max(parts) - min(parts) <= 1


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(12, 2) == [6, 6],\
        "Parts should be equal when value is divisible by parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(4, 1) == [4],\
        "When 'number_of_parts' = 1, part should be equal to value"
    assert split_integer(8, 1) == [8]
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]



def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(10, 3) == sorted(split_integer(10, 3))


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 3) == [0, 1, 1]
