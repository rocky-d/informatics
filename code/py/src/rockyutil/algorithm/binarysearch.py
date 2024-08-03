from bisect import bisect_left, bisect_right


def binary_search_cc(lo, hi, check):  # [lo, hi)
    hi -= 1
    while lo <= hi:  # [lo, hi]
        mid = lo + hi >> 1
        if check(mid):
            lo = mid + 1
        else:
            hi = mid - 1
    return lo


def binary_search_co(lo, hi, check):  # [lo, hi)
    while lo < hi:  # [lo, hi)
        mid = lo + hi >> 1
        if check(mid):
            lo = mid + 1
        else:
            hi = mid
    return lo  # return hi


def binary_search_oo(lo, hi, check):  # [lo, hi)
    lo -= 1
    while 1 < hi - lo:  # (lo, hi)
        mid = lo + hi >> 1
        if check(mid):
            lo = mid
        else:
            hi = mid
    return hi


if __name__ == '__main__':
    nums, target = [0, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9], 5
    lo, hi = 0, len(nums)
    key = lambda x: x
    check = lambda mid: key(nums[mid]) < target
    print(
        bisect_left(nums, target, lo = lo, hi = hi, key = key),
        bisect_left(range(hi), target, lo = lo, key = lambda mid: key(nums[mid])),
        lo + bisect_left(range(lo, hi), target, key = lambda mid: key(nums[mid])),
    )
    print(
        binary_search_cc(lo, hi, check),
        binary_search_co(lo, hi, check),
        binary_search_oo(lo, hi, check),
    )

    nums, target = [0, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9], 5
    lo, hi = 0, len(nums)
    key = lambda x: x
    check = lambda mid: key(nums[mid]) <= target
    print(
        bisect_right(nums, target, lo = lo, hi = hi, key = key),
        bisect_right(range(hi), target, lo = lo, key = lambda mid: key(nums[mid])),
        lo + bisect_right(range(lo, hi), target, key = lambda mid: key(nums[mid])),
    )
    print(
        binary_search_cc(lo, hi, check),
        binary_search_co(lo, hi, check),
        binary_search_oo(lo, hi, check),
    )
