from app.split_integer import split_integer

import pytest


@pytest.mark.parametrize(
    "value, nop, exp", [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6])
    ]
)
class Tests:
    def test_sum_of_the_parts_should_be_equal_to_value(
            self,
            value: int,
            nop: int,
            exp: list) -> None:
        assert sum(split_integer(value, nop)) == value

    def test_output_has_correct_number_of_parts(
            self,
            value: int,
            nop: int,
            exp: list) -> None:
        assert len(split_integer(value, nop)) == nop

    def test_difference_between_parts_is_at_most_one(
            self,
            value: int,
            nop: int,
            exp: list) -> None:
        assert max(split_integer(value, nop)) - \
            min(split_integer(value, nop)) <= 1

    def test_parts_should_be_sorted_when_they_are_not_equal(
            self,
            value: int,
            nop: int,
            exp: list) -> None:
        assert split_integer(value, nop) == sorted(split_integer(value, nop))

    def test_split_integer_returns_correct_result(
            self,
            value: int,
            nop: int,
            exp: list) -> None:
        assert split_integer(value, nop) == exp
