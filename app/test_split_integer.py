import pytest

from app.split_integer import split_integer


class TestSplitInteger:
    @pytest.mark.parametrize(
        "split_value,split_number_of_parts,split_parts",
        [
            pytest.param(
                6,
                2,
                [3, 3],
                id="sum of the parts should be equal to value"
            ),
            pytest.param(
                17,
                4,
                [4, 4, 4, 5],
                id=("should split into equal parts "
                    "when value divisible by parts")
            ),
            pytest.param(
                17,
                0,
                [],
                id=("should return part equals to "
                    "value when split into one part")
            ),
            pytest.param(
                32,
                6,
                [5, 5, 5, 5, 6, 6],
                id="parts should be sorted when they are not equal"
            ),
            pytest.param(
                2,
                6,
                [0, 0, 0, 0, 1, 1],
                id="should add zeros when value is less than number of parts"
            )
        ]
    )
    def test_result_corrected(
            self,
            split_value: int,
            split_number_of_parts: int,
            split_parts: list[int]
    ) -> None:

        assert split_integer(split_value, split_number_of_parts) == split_parts

# def test_sum_of_the_parts_should_be_equal_to_value() -> None:
#     value = 6
#     number_of_parts = 2
#
#     parts = split_integer(value, number_of_parts)
#
#     assert sum(parts) == value
#
#
# def test_should_split_into_equal_parts_when_value_divisible_by_parts(
#   ) -> None:
#     value = 17
#     number_of_parts = 4
#
#     parts = split_integer(value, number_of_parts)
#
#     assert max(parts) - min(parts) <= 1
#
#
# def test_should_return_part_equals_to_value_when_split_into_one_part(
#   ) -> None:
#     value = 17
#     number_of_parts = 0
#
#     parts = split_integer(value, number_of_parts)
#
#     assert len(parts) == 0
#
#
# def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
#     value = 32
#     number_of_parts = 6
#
#     parts = split_integer(value, number_of_parts)
#
#     assert parts == sorted(parts)
#
#
# def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
#     value = 2
#     number_of_parts = 6
#
#     parts = split_integer(value, number_of_parts)
#
#     if value < number_of_parts:
#         assert parts.count(0) == number_of_parts - value
