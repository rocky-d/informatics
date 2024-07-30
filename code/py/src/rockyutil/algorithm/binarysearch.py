from bisect import bisect_left, bisect_right


def binary_search_cc(lo, hi, check):
    hi -= 1
    while lo <= hi:  # [lo, hi]
        mid = lo + hi >> 1
        if check(mid):
            lo = mid + 1
        else:
            hi = mid - 1
    return lo


def binary_search_co(lo, hi, check):
    while lo < hi:  # [lo, hi)
        mid = lo + hi >> 1
        if check(mid):
            lo = mid + 1
        else:
            hi = mid
    return lo  # return hi


def binary_search_oo(lo, hi, check):
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
    print(bisect_left(nums, target, lo = lo, hi = hi, key = key))
    check = lambda idx: key(nums[idx]) < target
    print(binary_search_cc(lo = lo, hi = hi, check = check))
    print(binary_search_co(lo = lo, hi = hi, check = check))
    print(binary_search_oo(lo = lo, hi = hi, check = check))

    nums, target = [0, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9], 5
    lo, hi = 0, len(nums)
    key = lambda x: x
    print(bisect_right(nums, target, lo = lo, hi = hi, key = key))
    check = lambda idx: key(nums[idx]) <= target
    print(binary_search_cc(lo = lo, hi = hi, check = check))
    print(binary_search_co(lo = lo, hi = hi, check = check))
    print(binary_search_oo(lo = lo, hi = hi, check = check))
