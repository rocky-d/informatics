from rockyutil.leetcode import *


class CountIntervals:
    def __init__(self):
        self._sorted_dict = sc.SortedDict()
        self._count = 0

    def add(self, left: int, right: int) -> None:
        index = self._sorted_dict.bisect_left(left)
        while index < len(self._sorted_dict) and self._sorted_dict.values()[index] <= right:
            r, l = self._sorted_dict.items()[index]
            left, right = min(left, l), max(right, r)
            self._count -= r - l + 1
            self._sorted_dict.popitem(index)
        self._count += right - left + 1
        self._sorted_dict[right] = left

    def count(self) -> int:
        return self._count
