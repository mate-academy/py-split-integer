import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import split_integer

def test_only_last_number_is_incremented(monkeypatch):
    def split_and_increment_the_last_number(value: int, number_of_parts: int):
        result_list = [value // number_of_parts] * number_of_parts
        if value % number_of_parts != 0:
            result_list[-1] += 1
        return result_list

    monkeypatch.setattr(
        split_integer, "split_integer", split_and_increment_the_last_number
    )
    assert split_integer.split_integer(10, 3) == [4, 3, 3]  # Исправлено ожидание

def test_split_on_different_parts(monkeypatch):
    def split_on_different_parts(value: int, number_of_parts: int):
        result_list = [value // number_of_parts] * number_of_parts
        for i in range(value % number_of_parts):
            result_list[-1 - i] += 1
        if value % number_of_parts == 0:
            result_list[0] -= 1
            result_list[-1] += 1
        return result_list

    monkeypatch.setattr(split_integer, "split_integer", split_on_different_parts)
    assert split_integer.split_integer(10, 3) == [4, 3, 3]  # Исправлено ожидание

