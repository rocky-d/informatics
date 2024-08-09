def ternary_search_oo(lo, hi, check):  # [lo, hi)
    lo -= 1
    diff = hi - lo
    while 1 < hi - lo:  # (lo, hi)
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
    ...
