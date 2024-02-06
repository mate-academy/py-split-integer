import pytest
from app.split_integer import split_integer


class TestSplitInteger:
    @pytest.mark.parametrize(
        "value,number_of_parts,expected",
        [
            pytest.param(8, 1, 8,
                         id="sum of the parts should be equal to value"),
            pytest.param(6, 2, 6,
                         id="sum of the parts should be equal to value"),
            pytest.param(17, 4, 17,
                         id="sum of the parts should be equal to value"),
            pytest.param(32, 6, 32,
                         id="sum of the parts should be equal to value"),
            pytest.param(12, 3, [4, 4, 4],
                         id="should split into equal parts"),
            pytest.param(12, 2, [6, 6],
                         id="should split into equal parts"),
            pytest.param(8, 2, [4, 4],
                         id="should split into equal parts"),
            pytest.param(32, 6, [5, 5, 5, 5, 6, 6],
                         id="parts should be sorted"),
            pytest.param(17, 4, [4, 4, 4, 5],
                         id="parts should be sorted"),
            pytest.param(3, 5, [0, 0, 1, 1, 1],
                         id="should add zeros when value is less "
                            "than number of parts"),
            pytest.param(8, 1, 8,
                         id="should return part equals to value"),
        ]
    )
    def test_split_integer_behavior(
            self,
            value: int,
            number_of_parts: int,
            expected: int | list[int]
    ) -> None:
        result = split_integer(value, number_of_parts)
        if isinstance(expected, int):
            assert (sum(result) == expected)
        elif value < number_of_parts or number_of_parts == 1:
            assert (result == expected)
        else:
            assert (result == expected)
