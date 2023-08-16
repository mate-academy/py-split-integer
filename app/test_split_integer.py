from app.split_integer import split_integer


class TestSplitInteger:
    def test_sum_of_the_parts_should_be_equal_to_value(self) -> None:
        assert (
            sum(split_integer(32, 6)) == 32
        ), "Sum of parts should be equal to value"

    def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        self,
    ) -> None:
        assert split_integer(6, 2) == [
            3,
            3,
        ], "Should_split_into_equal_parts_when_value_divisible_by_parts"

    def test_should_return_part_equals_to_value_when_split_into_one_part(
        self,
    ) -> None:
        assert split_integer(8, 1) == [
            8
        ], "should_return_part_equals_to_value_when_split_into_one_part"

    def test_parts_should_be_sorted_when_they_are_not_equal(self) -> None:
        assert split_integer(32, 6) == [
            5,
            5,
            5,
            5,
            6,
            6,
        ], "parts_should_be_sorted_when_they_are_not_equal"

    def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        self,
    ) -> None:
        assert split_integer(3, 6) == [
            0,
            0,
            0,
            1,
            1,
            1,
        ], "should_add_zeros_when_value_is_less_than_number_of_parts"
