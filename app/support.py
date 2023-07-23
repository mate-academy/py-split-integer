from math import ceil


def splitting_list_into_two_equal_parts(input_list: list) -> tuple:
    if len(input_list) >= 1:
        middle = len(input_list) / 2
        right_side = round(middle)
        left_side = ceil(middle) if isinstance(middle, float) else right_side
        return input_list[:left_side], input_list[right_side:]
    raise Exception(("You use function "
                     "splitting_list_into_two_equal_parts incorrect!"))
