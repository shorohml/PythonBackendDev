"My custom list class"
from typing import Tuple


def _pad_list(
        src: list,
        target_len: int,
        val: int = 0) -> list:
    return [src[i] if i < len(src) else val for i in range(target_len)]


def _pad_lists(
        src_0: list,
        src_1: list,
        val: int = 0) -> Tuple[list, list, int]:
    res_len = max(len(src_0), len(src_1))
    src_0_pad, src_1_pad = src_0, src_1
    if len(src_0) < len(src_1):
        src_0_pad = _pad_list(src_0, res_len, val)
    else:
        src_1_pad = _pad_list(src_1, res_len, val)
    return src_0_pad, src_1_pad, res_len


class CustomList(list):

    "Custom list with support for +/-/comprehension"

    def __add__(self, other):
        self_pad, other_pad, res_len = _pad_lists(self, other)
        return CustomList((self_pad[i] + other_pad[i] for i in range(res_len)))

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        self_pad, other_pad, res_len = _pad_lists(self, other)
        return CustomList((self_pad[i] - other_pad[i] for i in range(res_len)))

    def __rsub__(self, other):
        self_pad, other_pad, res_len = _pad_lists(self, other)
        return CustomList((other_pad[i] - self_pad[i] for i in range(res_len)))

    def __lt__(self, other):
        sum_self, sum_other = sum(self), sum(other)
        return sum_self < sum_other

    def __gt__(self, other):
        sum_self, sum_other = sum(self), sum(other)
        return sum_self > sum_other

    def __le__(self, other):
        sum_self, sum_other = sum(self), sum(other)
        return sum_self <= sum_other

    def __ge__(self, other):
        sum_self, sum_other = sum(self), sum(other)
        return sum_self >= sum_other

    def __eq__(self, other):
        sum_self, sum_other = sum(self), sum(other)
        return sum_self == sum_other

    def __ne__(self, other):
        sum_self, sum_other = sum(self), sum(other)
        return sum_self != sum_other
