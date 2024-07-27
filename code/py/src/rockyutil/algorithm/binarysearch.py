def binary_search_cc(lo, hi, check):  # [lo, hi]
    while lo <= hi:
        mid = lo + hi >> 1
        if check(mid):
            lo = mid + 1
        else:
            hi = mid - 1
    return lo


def binary_search_co(lo, hi, check):  # [lo, hi)
    while lo < hi:
        mid = lo + hi >> 1
        if check(mid):
            lo = mid + 1
        else:
            hi = mid
    return lo  # return hi


def binary_search_oo(lo, hi, check):  # (lo, hi)
    while 1 < hi - lo:
        mid = lo + hi >> 1
        if check(mid):
            lo = mid
        else:
            hi = mid
    return hi


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9]
    n = len(nums)
    check = lambda idx: nums[idx] <= 5
    print(binary_search_cc(lo = 0, hi = n - 1, check = check))
    print(binary_search_co(lo = 0, hi = n, check = check))
    print(binary_search_oo(lo = -1, hi = n, check = check))
