import pytest

from app.split_integer import split_integer


class TestSplitInteger:
    @pytest.mark.parametrize(
        "initial_value,initial_number_of_parts,expected_list",
        [
            pytest.param(
                8,
                2,
                [4, 4],
                id="test should split into equal "
                   "parts when value divisible by parts"
            ),
            pytest.param(
                8,
                1,
                [8],
                id="test should return part equals "
                   "to value when split into one part"
            ),
            pytest.param(
                3,
                6,
                [0, 0, 0, 1, 1, 1],
                id="test should add zeros when"
                   " value is less than number of parts"
            )
        ]
    )
    def test_split_integers_correctly(
            self,
            initial_value: int,
            initial_number_of_parts: int,
            expected_list: list
    ) -> list:

        assert split_integer(initial_value, initial_number_of_parts) \
               == expected_list


class SumOfTheParts:
    @pytest.mark.parametrize(
        "initial_value,initial_number_of_parts,expected_sum",
        [
            pytest.param(
                9,
                3,
                9,
                id="test sum of the parts should be equal to value"
            )
        ]
    )
    def test_sum_of_the_parts(
            self,
            initial_value: int,
            initial_number: int,
            expected_sum: int
    ) -> int:

        assert sum(split_integer(initial_value, initial_number)) ==\
               expected_sum


class SortedWhenNotEqual:
    @pytest.mark.parametrize(
        "initial_value,initial_number_of_parts",
        [
            pytest.param(
                32,
                6,
                id="test parts should be sorted when they are not equal"
            )
        ]
    )
    def test_sorted_when_equal(
            self,
            initial_value: int,
            initial_number_of_parts: int
    ) -> bool:

        assert split_integer(initial_value,
               initial_number_of_parts) ==\
               sorted(split_integer(initial_value,
                      initial_number_of_parts))
