import unittest

from app.split_integer import split_integer


class TestSplitInteger(unittest.TestCase):
    def test_sum_of_the_parts_should_be_equal_to_value(self) -> None:
        self.assertEqual(sum(split_integer(17, 4)), 17)

    def test_should_split_into_equal_parts_when_value_divisible_by_parts(self) -> None:
        self.assertEqual(split_integer(6, 2), [3, 3])

    def test_should_return_part_equals_to_value_when_split_into_one_part(self) -> None:
        self.assertEqual(split_integer(8, 1), [8])

    def test_parts_should_be_sorted_when_they_are_not_equal(self) -> None:
        self.assertEqual(split_integer(20, 3), sorted(split_integer(20, 3)))

    def test_should_add_zeros_when_value_is_less_than_number_of_parts(self) -> None:
        self.assertEqual(split_integer(7, 12), [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1])


if __name__ == "__main__":
    unittest.main()
