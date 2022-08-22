from app.split_integer import split_integer
import pytest


class TestSplitInteger:
    @pytest.mark.parametrize(
        "value,number_of_parts,expected_result",
        [
            (32, 6, [5, 5, 5, 5, 6, 6]),
            (6, 2, [3, 3]),
            (8, 1, [8]),
            (17, 4, [4, 4, 4, 5]),
            (2, 5, [0, 0, 0, 1, 1])
        ]
    )
    def test_returns_correct_values(self,
                                    value,
                                    number_of_parts,
                                    expected_result):

        res = split_integer(value, number_of_parts)
        assert res == expected_result
