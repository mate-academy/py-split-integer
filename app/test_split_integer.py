from app.split_integer import split_integer
import pytest


class TestSplitIntegerClass:
    @pytest.mark.parametrize(
        "value, initial_element, expected_result",
        [
            pytest.param(16, 3, [5, 5, 6], id="test sum of the parts should be equal to value"),
            pytest.param(15, 2, [7, 8], id="test kek of the parts should be equal to value")
        ]
    )
    def test_split_integer(self, value: int, initial_element: int, expected_result: list):
        assert split_integer(value, initial_element) == expected_result

    @pytest.mark.parametrize(
        "value, initial_element, expected_result",
        [
            pytest.param(16, 3, 16, id="test sum of the parts should be equal to value"),
            pytest.param(15, 2, 15, id="test sum of the parts should be equal to value")
        ]
    )
    def test_split_integer_sum(self, value: int, initial_element: int, expected_result: int):
        assert sum(split_integer(value, initial_element)) == expected_result

    @pytest.mark.parametrize(
        "value, initial_element, expected_result",
        [
            pytest.param(15, 3, 3, id="test_should_split_into_equal_parts_when_value_divisible_by_parts"),
            pytest.param(10, 2, 2, id="test_should_split_into_equal_parts_when_value_divisible_by_parts")
        ]
    )
    def test_split_integer_equal_parts(self, value: int, initial_element: int, expected_result: int):
        assert len(split_integer(value, initial_element)) == expected_result

    @pytest.mark.parametrize(
        "value, initial_element, expected_result",
        [
            pytest.param(15, 1, [15], id="test_should_return_part_equals_to_value_when_split_into_one_part"),
            pytest.param(10, 1, [10], id="test_should_return_part_equals_to_value_when_split_into_one_part")
        ]
    )
    def test_split_integer_equals_to_value(self, value: int, initial_element: int, expected_result: list):
        assert split_integer(value, initial_element) == expected_result

    @pytest.mark.parametrize(
        "value, initial_element, expected_result",
        [
            pytest.param(15, 4, [3, 4, 4, 4], id="test_parts_should_be_sorted_when_they_are_not_equal"),
            pytest.param(10, 6, [1, 1, 2, 2, 2, 2], id="test_parts_should_be_sorted_when_they_are_not_equal")
        ]
    )
    def test_parts_should_be_sorted_when_they_are_not_equal(self, value: int, initial_element: int,
                                                            expected_result: list):
        assert split_integer(value, initial_element) == expected_result

    @pytest.mark.parametrize(
        "value, initial_element, expected_result",
        [
            pytest.param(10, 12, [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                         id="test_should_add_zeros_when_value_is_less_than_number_of_parts"),
            pytest.param(5, 15, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                         id="test_should_add_zeros_when_value_is_less_than_number_of_parts")
        ]
    )
    def test_should_add_zeros_when_value_is_less_than_number_of_parts(self, value: int, initial_element: int,
                                                                      expected_result: list):
        assert split_integer(value, initial_element) == expected_result
