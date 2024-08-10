from bisect import bisect_left, bisect_right


# [lo, hi]
def ternary_search_cc(lo, hi, check):  # [lo, hi)
    hi -= 1
    diff = hi - lo
    while -1 < diff:
        mid1 = lo + diff // 3
        mid2 = lo + (diff << 1) // 3
        res = check(mid1, mid2)
        if +1 == res:
            lo = mid2 + 1
        elif 0 == res:
            lo = mid1 + 1
            hi = mid2 - 1
        else:  # elif -1 == res:
            hi = mid1 - 1
        diff = hi - lo
    return lo


# [lo, hi)
def ternary_search_co(lo, hi, check):  # [lo, hi)
    diff = hi - lo
    while 0 < diff:
        mid1 = lo + diff // 3
        mid2 = lo + (diff << 1) // 3
        res = check(mid1, mid2)
        if +1 == res:
            lo = mid2 + 1
        elif 0 == res:
            lo = mid1 + 1
            hi = mid2
        else:  # elif -1 == res:
            hi = mid1
        diff = hi - lo
    return lo


# (lo, hi)
def ternary_search_oo(lo, hi, check):  # [lo, hi)
    lo -= 1
    diff = hi - lo
    while 1 < diff:
        mid1 = lo + diff // 3
        mid2 = lo + (diff << 1) // 3
        res = check(mid1, mid2)
        if +1 == res:
            lo = mid2
        elif 0 == res:
            lo = mid1
            hi = mid2
        else:  # elif -1 == res:
            hi = mid1
        diff = hi - lo
    return hi


if __name__ == '__main__':
    nums, target = [0, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9], 5
    lo, hi = 0, len(nums)
    key = lambda x: x
    func = lambda mid: key(nums[mid])
    check = lambda mid1, mid2: +1 if func(mid2) < target else 0 if func(mid1) < target else -1
    print(
        bisect_left(nums, target, lo = lo, hi = hi, key = key),
        bisect_left(range(hi), target, lo = lo, key = func),
        lo + bisect_left(range(lo, hi), target, key = func),
    )
    print(
        ternary_search_cc(lo, hi, check),
        ternary_search_co(lo, hi, check),
        ternary_search_oo(lo, hi, check),
    )

    nums, target = [0, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9], 5
    lo, hi = 0, len(nums)
    key = lambda x: x
    func = lambda mid: key(nums[mid])
    check = lambda mid1, mid2: +1 if func(mid2) <= target else 0 if func(mid1) <= target else -1
    print(
        bisect_right(nums, target, lo = lo, hi = hi, key = key),
        bisect_right(range(hi), target, lo = lo, key = func),
        lo + bisect_right(range(lo, hi), target, key = func),
    )
    print(
        ternary_search_cc(lo, hi, check),
        ternary_search_co(lo, hi, check),
        ternary_search_oo(lo, hi, check),
    )
