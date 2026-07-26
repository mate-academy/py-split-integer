import importlib


split_module = importlib.import_module("app.split_integer")


def is_ascending(arr: list[int]) -> bool:
    return all(a <= b for a, b in zip(arr, arr[1:]))


def test_sum_equals_value_and_length_is_parts() -> None:
    cases = [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (5, 5),
        (11, 5),
        (13, 5),
        (100, 3),
    ]
    for value, parts in cases:
        res = split_module.split_integer(value, parts)
        assert len(res) == parts
        assert sum(res) == value


def test_ascending_and_balanced_diff_le_1() -> None:
    cases = [(6, 4), (11, 5), (13, 5), (32, 6), (21, 7)]
    for value, parts in cases:
        res = split_module.split_integer(value, parts)
        assert is_ascending(res), "array must be sorted ascending"
        assert max(res) - min(res) <= 1, "max-min must be <= 1"


def test_when_divisible_all_parts_equal() -> None:

    value, parts = 12, 4
    res = split_module.split_integer(value, parts)
    assert len(set(res)) == 1, "all parts must be equal when value%parts==0"
    assert res == [3, 3, 3, 3]


def test_number_of_bigger_elements_equals_remainder() -> None:

    for value, parts in [(14, 5), (17, 4), (32, 6), (23, 7)]:
        base = value // parts
        rem = value % parts
        res = split_module.split_integer(value, parts)
        bigger = [x for x in res if x == base + 1]
        smaller = [x for x in res if x == base]
        assert len(bigger) == rem, "exactly 'rem' elements must be base+1"
        assert len(smaller) == parts - rem, \
            "rest must be exactly 'base' values"


def test_readme_examples_exact() -> None:
    assert split_module.split_integer(8, 1) == [8]
    assert split_module.split_integer(6, 2) == [3, 3]
    assert split_module.split_integer(17, 4) == [4, 4, 4, 5]
    assert split_module.split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
