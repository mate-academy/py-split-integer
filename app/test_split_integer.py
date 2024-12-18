import pytest


from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (1, 1),
        (6, 2),
        (17, 4),
        (32, 5),
        (100, 20)
    ]
)
def test_max_and_min_difference_should_be_less_that_one(
    value: int,
    number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert max(result) - min(result) <= 1, (
        "Difference of max and min number in the array should be <= 1"
    )


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (1, 1),
        (4, 2),
        (6, 2),
        (17, 4),
        (100, 20)
    ]
)


def test_sum_of_the_parts_should_be_equal_to_value(
    value: int,
    number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert sum(result) == value, "Sum of result list should be equal to value"


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (1, 1),
        (2, 2),
        (8, 4),
        (20, 5),
        (144, 12)
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int,
    number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)

    is_value_equal_to_all_parts = all(
        (value / number_of_parts) == part
        for part in result
    )
    assert is_value_equal_to_all_parts, (
        "Parts in result should be equal "
        "when value is divisible by number of parts"
    )
@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (1, 1),
        (2, 1),
        (8, 1),
        (11, 1),
        (101, 1)
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int,
    number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert len(result) == 1 and result[0] == value, (
        "Result list must have one part equal to value "
        "when number of parts == 1"
    )

    @pytest.mark.parametrize(
        "value,number_of_parts",
        [
            (3, 2),
            (10, 3),
            (17, 4),
            (25, 6),
            (100, 21)
        ]
    )
    def test_parts_should_be_sorted_when_they_are_not_equal(
            value: int,
            number_of_parts: int
    ) -> None:
        result = split_integer(value, number_of_parts)
        assert result == sorted(result), (
            "Result list must be sorted in ascending order if parts are not equal"
        )
@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (1, 2),
        (1, 10),
        (8, 9),
        (20, 25),
        (100, 102)
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value: int,
    number_of_parts: int
) -> None:
    result = split_integer(value=value, number_of_parts=number_of_parts)
    assert (
        len(result) == number_of_parts
        and result.count(0) == number_of_parts - value
    ), "Zeroes must be added to result when value < number_of_parts"
