import pytest


from app import split_integer  # <--- KLUCZOWE: import modułu, nie funkcji!


class TestSplitInteger:

    @pytest.mark.parametrize(
        "value, number_of_parts",
        [
            (17, 4),
            (21, 4),
            (6, 2),
            (12, 3),
            (100, 5),
            (30, 6),
        ]
    )
    def test_sum_and_distribution(
            self,
            value: int,
            number_of_parts: int
    ) -> None:
        result = split_integer.split_integer(value, number_of_parts)

        assert sum(result) == value
        assert len(result) == number_of_parts
        assert result == sorted(result)
        assert max(result) - min(result) <= 1

        if value % number_of_parts == 0:
            assert all(x == result[0] for x in result)

    @pytest.mark.parametrize(
        "value, number_of_parts",
        [
            (0, 5),
            (2, 5),
            (3, 5),
        ]
    )
    def test_small_values_with_zeros(
            self,
            value: int,
            number_of_parts: int
    ) -> None:
        result = split_integer.split_integer(value, number_of_parts)

        assert sum(result) == value
        assert len(result) == number_of_parts
        assert result == sorted(result)
        assert all(x in (0, 1) for x in result)
