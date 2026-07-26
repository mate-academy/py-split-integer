import pytest
from app.split_integer import split_integer

Datas = [
    (8, 1),
    (6, 2),
    (17, 4),
    (32, 6),
    (2, 5),
    (11, 3),
    (0, 5),
]


@pytest.mark.parametrize("value, number_of_parts", Datas)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int,
    number_of_parts: int,
) -> None:
    result = split_integer(value, number_of_parts)

    assert len(result) == number_of_parts
    assert sum(result) == value
    assert max(result) - min(result) <= 1

    base = value // number_of_parts
    remainder = value % number_of_parts

    expected = [base] * number_of_parts
    for i in range(remainder):
        expected[number_of_parts - 1 - i] += 1

    assert result == expected


@pytest.mark.parametrize("value, number_of_parts", Datas)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int,
    number_of_parts: int,
) -> None:
    if value % number_of_parts == 0:
        result = split_integer(value, number_of_parts)
        expected = value // number_of_parts

        for part in result:
            assert part == expected

        assert result == sorted(result)


@pytest.mark.parametrize("value, number_of_parts", Datas)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int,
    number_of_parts: int,
) -> None:
    if number_of_parts == 1:
        result = split_integer(value, number_of_parts)
        assert result == [value]


@pytest.mark.parametrize("value, number_of_parts", Datas)
def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int,
    number_of_parts: int,
) -> None:
    result = split_integer(value, number_of_parts)

    base = value // number_of_parts
    remainder = value % number_of_parts

    assert result == sorted(result)
    assert result.count(base + 1) == remainder
    assert result.count(base) == number_of_parts - remainder


@pytest.mark.parametrize("value, number_of_parts", Datas)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value: int,
    number_of_parts: int,
) -> None:
    result = split_integer(value, number_of_parts)

    if value < number_of_parts:
        assert result.count(0) == (number_of_parts - value)
        assert result.count(1) == value
        assert sum(result) == value
        assert result == sorted(result)
