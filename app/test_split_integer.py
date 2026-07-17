from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value, num_of_parts = 17, 4
    assert (
        split_integer(value, num_of_parts) == [4, 4, 4, 5],
        "Sum of the parts should be equal to value"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value, num_of_parts = 36, 6
    assert (
        split_integer(value, num_of_parts) == [6, 6, 6, 6, 6, 6],
        "Value divisible by parts should be split into equal parts"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value, num_of_parts = 8, 1
    assert (
        split_integer(value, num_of_parts) == [8],
        "Return part equals to value when split into one part"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value, num_of_parts = 32, 6
    assert (
        split_integer(value, num_of_parts) == [5, 5, 5, 5, 6, 6],
        "Parts sorted when they are not equal"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value, num_of_parts = 1, 2
    assert(
        split_integer(value, num_of_parts) == [0, 1],
        "Adding zeros when value is less than number of parts"
    )


# result:
# split_integer(8, 1) == [8]
# split_integer(6, 2) == [3, 3]
# split_integer(17, 4) == [4, 4, 4, 5]
# split_integer(32, 6) == [5, 5, 5, 5, 6, 6]

# Write tests for split_integer function that takes 2 positive integers value and number_of_parts and returns an array containing exactly number_of_parts integer elements:

# the difference between the max and min number in the array should be <= 1;
# the array should be sorted ascending (from lowest to highest).
# Please note: you have to use pytest for writing tests.

# You don't need to validate arguments (they are always valid).

# Notes:

# write tests in the /app/test_split_integer.py module;
# their names indicate what exactly they should test.
# Run pytest app/ to check if function pass your tests.

# Run pytest --numprocesses=auto tests/ to check if your tests cover all boundary conditions and pass task tests.