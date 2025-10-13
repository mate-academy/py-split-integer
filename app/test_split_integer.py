from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    """Test that sum of all parts equals the original value"""
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(6, 2)) == 6
    assert sum(split_integer(32, 6)) == 32
    assert sum(split_integer(3, 5)) == 3
    assert sum(split_integer(0, 5)) == 0
    assert sum(split_integer(1, 1)) == 1
    assert sum(split_integer(100, 9)) == 100
    assert sum(split_integer(10, 3)) == 10


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    """Test that when value is divisible by parts, all elements are equal"""
    result = split_integer(6, 2)
    assert result == [3, 3]
    assert len(set(result)) == 1, "All elements must be identical when value is divisible by parts"
    
    result = split_integer(12, 4)
    assert result == [3, 3, 3, 3]
    assert len(set(result)) == 1, "All elements must be identical when value is divisible by parts"
    
    result = split_integer(20, 5)
    assert result == [4, 4, 4, 4, 4]
    assert len(set(result)) == 1, "All elements must be identical when value is divisible by parts"
    
    result = split_integer(100, 10)
    assert len(set(result)) == 1, "All elements must be identical when value is divisible by parts"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    """Test splitting into a single part returns the value itself"""
    assert split_integer(8, 1) == [8]
    assert split_integer(1, 1) == [1]
    assert split_integer(100, 1) == [100]


def test_parts_should_be_sorted_ascending() -> None:
    """Test that result is always sorted in ascending order"""
    result = split_integer(17, 4)
    assert result == sorted(result)
    
    result = split_integer(32, 6)
    assert result == sorted(result)
    
    result = split_integer(10, 3)
    assert result == sorted(result)


def test_difference_between_max_and_min_should_be_at_most_one() -> None:
    """Test that max - min <= 1 for all splits"""
    test_cases = [(17, 4), (32, 6), (3, 5), (100, 9), (0, 5), (1, 3), (10, 3)]
    for value, parts in test_cases:
        result = split_integer(value, parts)
        if len(result) > 0:
            diff = max(result) - min(result)
            assert diff <= 1, f"Difference is {diff} for split_integer({value}, {parts}), expected <= 1"


def test_correct_number_of_parts_returned() -> None:
    """Test that exactly number_of_parts elements are returned"""
    assert len(split_integer(17, 4)) == 4
    assert len(split_integer(32, 6)) == 6
    assert len(split_integer(10, 3)) == 3
    assert len(split_integer(8, 1)) == 1


def test_split_10_into_3_parts() -> None:
    """Test splitting 10 into 3 parts: should be [3, 3, 4]"""
    result = split_integer(10, 3)
    assert result == [3, 3, 4], f"Expected [3, 3, 4] but got {result}"


def test_split_11_into_3_parts() -> None:
    """Test splitting 11 into 3 parts: should be [3, 4, 4]"""
    result = split_integer(11, 3)
    assert result == [3, 4, 4], f"Expected [3, 4, 4] but got {result}"


def test_split_17_into_4_parts() -> None:
    """Test splitting 17 into 4 parts: should be [4, 4, 4, 5]"""
    result = split_integer(17, 4)
    assert result == [4, 4, 4, 5], f"Expected [4, 4, 4, 5] but got {result}"


def test_split_32_into_6_parts() -> None:
    """Test splitting 32 into 6 parts: should be [5, 5, 5, 5, 6, 6]"""
    result = split_integer(32, 6)
    assert result == [5, 5, 5, 5, 6, 6], f"Expected [5, 5, 5, 5, 6, 6] but got {result}"


def test_split_3_into_5_parts() -> None:
    """Test splitting 3 into 5 parts: should be [0, 0, 1, 1, 1]"""
    result = split_integer(3, 5)
    assert result == [0, 0, 1, 1, 1], f"Expected [0, 0, 1, 1, 1] but got {result}"


def test_count_of_larger_elements_equals_remainder() -> None:
    """Test that count of larger elements equals the remainder"""
    # 10 = 3*3 + 1, so one element should be 4, two should be 3
    result = split_integer(10, 3)
    assert result.count(4) == 1, "Should have exactly 1 element equal to 4"
    assert result.count(3) == 2, "Should have exactly 2 elements equal to 3"
    
    # 11 = 3*3 + 2, so two elements should be 4, one should be 3
    result = split_integer(11, 3)
    assert result.count(4) == 2, "Should have exactly 2 elements equal to 4"
    assert result.count(3) == 1, "Should have exactly 1 element equal to 3"
    
    # 17 = 4*4 + 1, so one element should be 5, three should be 4
    result = split_integer(17, 4)
    assert result.count(5) == 1, "Should have exactly 1 element equal to 5"
    assert result.count(4) == 3, "Should have exactly 3 elements equal to 4"
    
    # 32 = 6*5 + 2, so two elements should be 6, four should be 5
    result = split_integer(32, 6)
    assert result.count(6) == 2, "Should have exactly 2 elements equal to 6"
    assert result.count(5) == 4, "Should have exactly 4 elements equal to 5"


def test_examples_from_specification() -> None:
    """Test all examples provided in the specification"""
    assert split_integer(8, 1) == [8]
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]