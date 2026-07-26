from app.split_integer import split_integer


def test_split_integer_single_part() -> None:
    """Test splitting a number into a single part."""
    assert split_integer(8, 1) == [8]
    assert split_integer(1, 1) == [1]
    assert split_integer(100, 1) == [100]


def test_split_integer_equal_parts() -> None:
    """Test splitting a number into equal parts (no remainder)."""
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(10, 5) == [2, 2, 2, 2, 2]
    assert split_integer(12, 3) == [4, 4, 4]
    assert split_integer(20, 4) == [5, 5, 5, 5]


def test_split_integer_with_remainder() -> None:
    """Test splitting a number with remainder."""
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    assert split_integer(13, 5) == [2, 2, 3, 3, 3]
    assert split_integer(11, 3) == [3, 4, 4]


def test_split_integer_small_numbers() -> None:
    """Test splitting small numbers."""
    assert split_integer(2, 2) == [1, 1]
    assert split_integer(3, 2) == [1, 2]
    assert split_integer(5, 3) == [1, 2, 2]
    assert split_integer(7, 4) == [1, 2, 2, 2]


def test_split_integer_large_parts() -> None:
    """Test splitting into many parts."""
    result_10_10 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert split_integer(10, 10) == result_10_10

    result_15_10 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    assert split_integer(15, 10) == result_15_10

    result_7_7 = [1, 1, 1, 1, 1, 1, 1]
    assert split_integer(7, 7) == result_7_7


def test_split_integer_edge_cases() -> None:
    """Test edge cases."""
    # Number equals parts
    assert split_integer(5, 5) == [1, 1, 1, 1, 1]
    assert split_integer(3, 3) == [1, 1, 1]

    # Large number, few parts
    assert split_integer(100, 3) == [33, 33, 34]
    assert split_integer(101, 3) == [33, 34, 34]

    # Prime numbers
    assert split_integer(7, 2) == [3, 4]
    assert split_integer(11, 4) == [2, 3, 3, 3]


def test_split_integer_properties() -> None:
    """Test that the function satisfies all required properties."""
    test_cases = [
        (8, 1), (6, 2), (17, 4), (32, 6), (13, 5), (11, 3),
        (100, 7), (50, 8), (25, 4), (30, 7), (99, 10)
    ]

    for value, parts in test_cases:
        result = split_integer(value, parts)

        # Check correct number of parts
        expected_parts = parts
        actual_parts = len(result)
        assert actual_parts == expected_parts, (
            f"Expected {expected_parts} parts, got {actual_parts}"
        )

        # Check sum equals original value
        result_sum = sum(result)
        assert result_sum == value, f"Sum {result_sum} != {value}"

        # Check sorted ascending
        sorted_result = sorted(result)
        assert result == sorted_result, f"Array not sorted: {result}"

        # Check max - min <= 1
        if len(result) > 1:
            max_val = max(result)
            min_val = min(result)
            difference = max_val - min_val
            assert difference <= 1, f"Difference > 1: {result}"

        # Check all elements are positive
        positive_check = all(x > 0 for x in result)
        assert positive_check, f"Non-positive elements: {result}"


def test_split_integer_mathematical_correctness() -> None:
    """Test mathematical properties of the split."""
    # When remainder is 0, all parts should be equal
    assert split_integer(12, 4) == [3, 3, 3, 3]
    assert split_integer(20, 5) == [4, 4, 4, 4, 4]

    # When remainder is r, exactly r parts should be (base + 1)
    result = split_integer(23, 7)  # 23 = 7*3 + 2, base=3, remainder=2
    count_base = result.count(3)
    count_base_plus_one = result.count(4)
    assert count_base == 5  # 7-2 = 5 parts with base value
    assert count_base_plus_one == 2  # 2 parts with base+1 value

    result = split_integer(19, 5)  # 19 = 5*3 + 4, base=3, remainder=4
    count_base = result.count(3)
    count_base_plus_one = result.count(4)
    assert count_base == 1  # 5-4 = 1 part with base value
    assert count_base_plus_one == 4  # 4 parts with base+1 value


def test_split_integer_boundary_conditions() -> None:
    """Test boundary conditions and special cases."""
    # Minimum valid inputs
    assert split_integer(1, 1) == [1]
    assert split_integer(2, 1) == [2]

    # Large numbers
    result_1000_7 = split_integer(1000, 7)
    assert len(result_1000_7) == 7
    assert sum(result_1000_7) == 1000
    assert max(result_1000_7) - min(result_1000_7) <= 1

    # Additional test cases
    assert split_integer(50, 7) == [7, 7, 7, 7, 7, 7, 8]
    assert split_integer(29, 6) == [4, 5, 5, 5, 5, 5]
