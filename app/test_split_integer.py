from app.split_integer import split_integer


class TestSplitInteger:
    def test_sum_or_the_parts_should_be_equal_to_value(self):
        assert sum(split_integer(17, 4)) == 17

    def test_split_into_equal_parts_when_value_is_divisible_by_parts(self):
        assert split_integer(16, 4) == [4, 4, 4, 4]

    def test_return_part_equals_to_a_value_when_slitting_into_one_part(self):
        assert split_integer(8, 1) == [8]

    def test_parts_should_be_sorted_when_they_are_not_equal(self):
        assert split_integer(14, 4) == sorted(split_integer(14, 4))

    def test_should_add_zeros_when_value_is_less_than_number_of_parts(self):
        assert split_integer(3, 5) == [0, 0, 1, 1, 1]
