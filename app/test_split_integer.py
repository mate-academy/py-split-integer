import pytest

from app.split_integer import split_integer


class TestSplitInteger:
    @pytest.mark.parametrize(
        "value,number_of_parts,expected_result",
        [
            (8, 1, [8]),
        ]
        # (6, 2, [3, 3]),
        # (17, 4, [4, 4, 4, 5]),
        # (32, 6, [5, 5, 5, 5, 6, 6])
    )
    def test_sum_of_the_parts_should_be_equal_to_value(self, value, number_of_parts, expected_result) -> None:
        assert sum(split_integer(value, number_of_parts)) == value

    @pytest.mark.parametrize(
        "value,number_of_parts,expected_result",
        [
            (9, 3, [3, 3, 3]),
        ]
    )
    def test_should_split_into_equal_parts_when_value_divisible_by_parts(self, value, number_of_parts,
                                                                         expected_result) -> None:
        assert split_integer(value, number_of_parts) == expected_result
    @pytest.mark.parametrize(
        "value,number_of_parts,expected_result",
        [
            (8, 1, [8]),
        ]
    )
    def test_should_return_part_equals_to_value_when_split_into_one_part(self, value, number_of_parts,
                                                                         expected_result) -> None:
        assert split_integer(value, number_of_parts) == expected_result
        assert len(split_integer(value, number_of_parts)) == 1

    @pytest.mark.parametrize(
        "value,number_of_parts,expected_result",
        [
            (17, 4, [4, 4, 4, 5]),
        ]
    )
    def test_parts_should_be_sorted_when_they_are_not_equal(self, value, number_of_parts, expected_result) -> None:
        assert split_integer(value, number_of_parts, ) == expected_result

    @pytest.mark.parametrize(
        "value,number_of_parts,expected_result",
        [
            (4, 6, [0, 0, 1, 1, 1, 1]),
        ]
    )
    def test_should_add_zeros_when_value_is_less_than_number_of_parts(self, value, number_of_parts,
                                                                      expected_result) -> None:
        assert split_integer(value, number_of_parts) == expected_result
        assert expected_result[0] == 0
        assert expected_result[1] == 0
