def binary_search_cc(lft, rit, check):  # [lft, rit]
    while lft <= rit:
        mid = lft + rit >> 1
        if check(mid):
            lft = mid + 1
        else:
            rit = mid - 1
    return lft


def binary_search_co(lft, rit, check):  # [lft, rit)
    while lft < rit:
        mid = lft + rit >> 1
        if check(mid):
            lft = mid + 1
        else:
            rit = mid
    return lft  # return rit


def binary_search_oo(lft, rit, check):  # (lft, rit)
    while lft + 1 < rit:
        mid = lft + rit >> 1
        if check(mid):
            lft = mid
        else:
            rit = mid
    return rit


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9]
    n = len(nums)
    check = lambda idx: nums[idx] < 5
    print(binary_search_cc(lft = 0, rit = n - 1, check = check))
    print(binary_search_co(lft = 0, rit = n, check = check))
    print(binary_search_oo(lft = -1, rit = n, check = check))
