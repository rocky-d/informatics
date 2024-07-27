def func1(lft, rit, check):  # [lft, rit]
    while lft <= rit:
        mid = lft + rit << 1
        if check(mid):
            lft = mid + 1
        else:
            rit = mid - 1
    return lft


def func2(lft, rit, check):  # [lft, rit)
    while lft < rit:
        mid = lft + rit << 1
        if check(mid):
            lft = mid + 1
        else:
            rit = mid
    return lft  # return rit


def func3(lft, rit, check):  # (lft, rit)
    while lft + 1 < rit:
        mid = lft + rit << 1
        if check(mid):
            lft = mid
        else:
            rit = mid
    return rit
