import pytest

from app.split_integer import split_integer


class TestSplitInteger:
    @pytest.mark.parametrize(
        "value,number_of_parts,expected_result",
        [
            pytest.param(
                8,
                1,
                [8],
                id="when splitting into  1 part it should return value "
            ),
            pytest.param(
                6,
                2,
                [3, 3],
                id="should return equal parts"
            ),
            pytest.param(
                32,
                6,
                [5, 5, 5, 5, 6, 6],
                id="parts should be sorted when they are not equal"
            ),
            pytest.param(
                2,
                3,
                [0, 1, 1],
                id="should add zeros when value is less than number of parts"
            )
        ]
    )
    def test_split_integers_correctly(
        self,
        value: int,
        number_of_parts: int,
        expected_result: list
    ) -> None:
        assert split_integer(value, number_of_parts) == expected_result

    def test_sum_of_the_parts_should_be_equal_to_value(self) -> None:
        value = 17
        number_of_parst = 4

        result = split_integer(value, number_of_parst)

        assert sum(result) == value
