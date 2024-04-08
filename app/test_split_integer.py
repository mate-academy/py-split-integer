import unittest
from app.split_integer import split_integer


class TestSplitInteger(unittest.TestCase):

    def test_split_integer(self) -> None:
        """
        Test for split_integer function.
        """
        test_cases = [
            (8, 1, [8]),
            (6, 2, [3, 3]),
            (17, 4, [4, 4, 4, 5]),
            (32, 6, [5, 5, 5, 5, 6, 6])
        ]

        for value, number_of_parts, expected_result in test_cases:
            with self.subTest(
                    value=value,
                    number_of_parts=number_of_parts,
                    expected_result=expected_result
            ):
                self.assertEqual(split_integer(
                    value, number_of_parts),
                    expected_result
                )


if __name__ == "__main__":
    unittest.main()
