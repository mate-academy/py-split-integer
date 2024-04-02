import pytest

from app.split_integer import split_integer


class TestSplit:

    @pytest.mark.parametrize(
        "first_int, second_int, result",
        [
            (8, 1, [8]),
            (6, 2, [3, 3]),
            (17, 4, [4, 4, 4, 5]),
            (32, 6, [5, 5, 5, 5, 6, 6])
        ],
        ids=["First int is 8, second int is 1",
             "First int is 6, second int is 2",
             "First int is 17, second int is 4",
             "First int is 32, second int is 6"]
    )
    def test_sum_of_the_parts_should_be_equal_to_value(
            self,
            first_int: int,
            second_int: int,
            result: list
    ) -> None:
        assert split_integer(first_int, second_int) == result

    @pytest.mark.parametrize(
        "first_int, second_int, expected_result",
        [
            (6, 2, [3, 3])
        ],
        ids=["First int is 6, second int is 2"]
    )
    def test_should_split_into_equal_parts_when_value_divisible_by_parts(
            self,
            first_int: int,
            second_int: int,
            expected_result: list
    ) -> None:
        assert (split_integer(first_int, second_int) == expected_result
                ), "Test should split equal parts when value is divisible by"

    def test_should_return_part_equals_to_value_when_split_into_one_part(
            self
    ) -> None:
        first_int = 8
        second_int = 1
        assert (split_integer(first_int, second_int) == [8]
                ), "Test should return part equals to value"

    def test_parts_should_be_sorted_when_they_are_not_equal(self) -> None:
        first_int = 17
        second_int = 4
        result = [4, 4, 4, 5]
        assert (split_integer(first_int, second_int) == sorted(result)
                ), "Test parts should be sorted when they are not equal"

    @pytest.mark.parametrize(
        "first_int, second_int, expected_result",
        [
            (3, 5, [0, 0, 1, 1, 1])
        ],
        ids=["First int is 3, second int is 5"]
    )
    def test_should_add_zeros_when_value_is_less_than_number_of_parts(
            self,
            first_int: int,
            second_int: int,
            expected_result: list
    ) -> None:
        assert (split_integer(first_int, second_int) == expected_result
                ), "Test should add zeros"
