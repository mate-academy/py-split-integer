from app.split_integer import split_integer


# @pytest.mark.parametrize(
#     "value, number_of_parts, expected_result",
#     [
#         (10, 5, 10),
#         (11, 5, 11),
#         (10, 10, 10),
#         (10, 1, 10)
#     ],
#     ids=["value % number_of_parts = 0",
#          "value % number_of_parts != 0",
#          "value = number_of_parts",
#          "value in expected_result",
#          ]
# )
# def test_sum_of_the_parts_should_be_equal_to_value(value: int,
#                                                    number_of_parts: int,
#                                                    expected_result: list[int]
#                                                    ) -> None:
#     assert sum(split_integer(value, number_of_parts)) == expected_result

# @pytest.mark.parametrize(
#     "value, number_of_parts, expected_result",
#     [
#         (1, 1, [1]),
#         (10, 5, [2, 2, 2, 2, 2]),
#         (10, 10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
#         (10, 1, [10])
#     ],
#     ids=["value = 1 and value % number_of_parts == 0",
#          "value % number_of_parts == 0",
#          "value = number_of_parts",
#          "value in expected_result",
#          ]
# )
# def test_should_split_into_equal_parts_when_value_divisible_by_parts(value: int,
#                                                                      number_of_parts: int,
#                                                                      expected_result: list[int]
#                                                                      ) -> None:
#     assert set(split_integer(value, number_of_parts)).pop() == set(expected_result).pop()

def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    for value in range(1, 4):
        result = split_integer(value, 1)
        assert len(result) == 1 and result[0] == value
#
#
# def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
#     value, number_of_parts = 0, 0
#     result = split_integer(value, number_of_parts)
#
#
# def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
#     value, number_of_parts = 0, 0
#     result = split_integer(value, number_of_parts)
