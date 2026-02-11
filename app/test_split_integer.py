import pytest


from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        pytest.param(
            8,
            1,
            id="one_divisible"
        ),
        pytest.param(
            6,
            2,
            id="divisible"
        ),
        pytest.param(
            17,
            4,
            id="not_divisible"
        )
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert sum(result) == value


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        pytest.param(
            8,
            1,
            id="one_divisible"
        ),
        pytest.param(
            6,
            2,
            id="divisible"
        )
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert max(result) == min(result)


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        pytest.param(
            8,
            1,
            id="equal"
        ),
        pytest.param(
            6,
            1,
            id="equal"
        ),
        pytest.param(
            17,
            1,
            id="equal"
        )
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int,
        number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert len(result) == 1
    assert result[0] == value


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        pytest.param(
            17,
            4,
            id="sorted without problems"
        ),
        pytest.param(
            32,
            6,
            id="sorted without problems"
        )
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    assert sum(result) == value


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        pytest.param(
            3,
            5,
            id="should be zeros"
        ),
        pytest.param(
            2,
            4,
            id="should be zeros"
        ),
        pytest.param(
            1,
            3,
            id="should be zeros"
        )
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)

    assert len(result) == number_of_parts
    assert sum(result) == value
    assert max(result) - min(result) <= 1
    assert result == sorted(result)
