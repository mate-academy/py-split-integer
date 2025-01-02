from app.split_integer import split_integer
import pytest


class TestSplitInteger:
    @pytest.mark.parametrize(
        "value, initial_element, expected_result",
        [
            pytest.param(16, 3, [5, 5, 6],
                         id="test sum of parts equals value"),
            pytest.param(15, 2, [7, 8],
                         id="test sum of parts equals value")
        ]
    )
    def test_split(self, value: int,
                   initial_element: int,
                   expected_result: list) -> None:
        assert split_integer(value, initial_element) == expected_result

    @pytest.mark.parametrize(
        "value, initial_element, expected_result",
        [
            pytest.param(16, 3, 16,
                         id="test sum of parts equals value"),
            pytest.param(15, 2, 15,
                         id="test sum of parts equals value")
        ]
    )
    def test_sum(self, value: int,
                 initial_element: int,
                 expected_result: int) -> None:
        assert sum(split_integer(value, initial_element)) == expected_result

    @pytest.mark.parametrize(
        "value, initial_element, expected_result",
        [
            pytest.param(15, 3, 3, id="test equal parts when divisible"),
            pytest.param(10, 2, 2, id="test equal parts when divisible")
        ]
    )
    def test_equal_parts(self, value: int,
                         initial_element: int,
                         expected_result: int) -> None:
        assert len(split_integer(value, initial_element)) == expected_result

    @pytest.mark.parametrize(
        "value, initial_element, expected_result",
        [
            pytest.param(15, 1, [15],
                         id="test one part equals value"),
            pytest.param(10, 1, [10],
                         id="test one part equals value")
        ]
    )
    def test_single_part(self, value: int,
                         initial_element: int,
                         expected_result: list) -> None:
        assert split_integer(value, initial_element) == expected_result

    @pytest.mark.parametrize(
        "value, initial_element, expected_result",
        [
            pytest.param(15, 4, [3, 4, 4, 4],
                         id="test sorted parts when unequal"),
            pytest.param(10, 6, [1, 1, 2, 2, 2, 2],
                         id="test sorted parts when unequal")
        ]
    )
    def test_sorted_parts(self, value: int,
                          initial_element: int,
                          expected_result: list) -> None:
        assert split_integer(value, initial_element) == expected_result

    @pytest.mark.parametrize(
        "value, initial_element, expected_result",
        [
            pytest.param(10, 12, [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                         id="test add zeros when value is less than parts"),
            pytest.param(5, 15, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                         id="test add zeros when value is less than parts")
        ]
    )
    def test_add_zeros(self, value: int,
                       initial_element: int,
                       expected_result: list) -> None:
        assert split_integer(value, initial_element) == expected_result
