import pytest
from app.split_integer import split_integer


class TestSplitIntegerClass():
    @pytest.mark.parametrize(
        "value, number_of_parts, expected_result",
        [
            pytest.param(17, 4, 17,
                         id="sum of the parts should be equal to value"),
            pytest.param(32, 6, 32,
                         id="sum of the parts should be equal to value"),
            pytest.param(25, 5, [5, 5, 5, 5, 5],
                         id="should split into equal parts"),
            pytest.param(18, 6, [3, 3, 3, 3, 3, 3],
                         id="should split into equal parts"),
            pytest.param(8, 1, 8,
                         id="should return part equals to value "),
            pytest.param(3, 1, 3,
                         id="should return part equals to value "),
            pytest.param(17, 4, [4, 4, 4, 5],
                         id="parts should be sorted"),
            pytest.param(32, 6, [5, 5, 5, 5, 6, 6],
                         id="parts should be sorted"),
            pytest.param(3, 5, [0, 0, 1, 1, 1],
                         id="should add zeros"),
            pytest.param(4, 7, [0, 0, 0, 1, 1, 1, 1],
                         id="should add zeros"),
        ]
    )
    def test_return_values_correctly(
            self,
            value: int,
            number_of_parts: int,
            expected_result: list[int] | int
    ) -> None:
        result = split_integer(value, number_of_parts)
        if isinstance(expected_result, int):
            assert sum(result) == expected_result
        else:
            assert result == expected_result
