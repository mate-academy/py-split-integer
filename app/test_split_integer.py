import pytest
import app.split_integer as split_module


def split(value: int, parts: int) -> list[int]:
    return split_module.split_integer(value, parts)


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    cases = [
        (8, 3),
        (17, 4),
        (6, 2),
        (32, 6),
        (3, 5),
        (2, 4),
    ]
    for value, parts in cases:
        result = split(value, parts)
        assert sum(result) == value, (
            f"For split({value}, {parts}) sum={sum(result)} "
            f"but expected {value}"
        )


def test_length_of_result_should_equal_number_of_parts() -> None:
    cases = [
        (8, 3),
        (17, 4),
        (6, 2),
        (32, 6),
        (3, 5),
        (2, 4),
    ]
    for value, parts in cases:
        result = split(value, parts)
        assert len(result) == parts, (
            f"For split({value}, {parts}) length={len(result)} "
            f"but expected {parts}"
        )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split(6, 2) == [3, 3]
    assert split(8, 4) == [2, 2, 2, 2]
    assert split(10, 5) == [2, 2, 2, 2, 2]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split(8, 1) == [8]
    assert split(15, 1) == [15]


def test_parts_should_be_sorted_and_diff_at_most_one() -> None:
    result = split(17, 4)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split(3, 5) == [0, 0, 1, 1, 1]
    assert split(2, 4) == [0, 0, 1, 1]


@pytest.mark.parametrize(
    "value, parts, expected",
    [
        (18, 4, [4, 4, 5, 5]),
        (19, 4, [4, 5, 5, 5]),
        (20, 6, [3, 3, 3, 3, 4, 4]),
    ],
)
def test_should_evenly_distribute_remainder(
    value: int, parts: int, expected: list[int]
) -> None:
    result = split(value, parts)
    assert result == expected, (
        f"For split({value}, {parts}) got {result}, "
        f"expected {expected}"
    )
