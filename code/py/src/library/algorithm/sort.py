from copy import copy
from operator import gt, lt


def quick_sort(nums, /, *, key=None, reverse=False, inplace=False):
    key = key if key is not None else lambda x: x
    cmp = gt if reverse else lt
    nums = nums if inplace else copy(nums)

    def _partition(lo, hi):
        base = nums[hi]
        pivot = lo
        for i in range(lo, hi):
            if not cmp(key(nums[i]), key(base)):
                continue
            nums[pivot], nums[i] = nums[i], nums[pivot]
            pivot += 1
        nums[pivot], nums[hi] = nums[hi], nums[pivot]
        return pivot

    def _quick_sort(lo, hi):
        if not lo < hi:
            return
        pivot = _partition(lo, hi)
        _quick_sort(lo, pivot - 1)
        _quick_sort(pivot + 1, hi)

    _quick_sort(0, len(nums) - 1)
    return None if inplace else nums


def merge_sort(nums, /, *, key=None, reverse=False, inplace=False):
    pass


if __name__ == '__main__':
    nums = [6, 2, 5, 9, 1, 5, 8, 3]
    print(quick_sort(nums))
