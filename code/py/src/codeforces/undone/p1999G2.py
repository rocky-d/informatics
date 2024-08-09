def check(mid1: int, mid2: int) -> int:
    if mid1 > mid2:
        mid1, mid2 = mid2, mid1
    print('?', mid1, mid2, flush = True)
    x = int(input())
    if x == (mid1 + 1) * (mid2 + 1):
        res = -1
    elif x == mid1 * (mid2 + 1):
        res = 0
    else:  # elif x == mid1 * mid2:
        res = +1
    return res


def main() -> None:
    lo1, hi1 = 1, 1000
    lo2, hi2 = 1, 1000
    while 1 < hi1 - lo1 and 1 < hi2 - lo2:
        mid1 = lo1 + (hi1 - lo1) // 3
        mid2 = lo2 + 2 * (hi2 - lo2) // 3
        res = check(mid1 = mid1, mid2 = mid2)
        if -1 == res:
            hi1 = mid1
            hi2 = mid2
        elif 0 == res:
            if mid1 > mid2:
                hi1 = mid1
                lo2 = mid2
            else:
                lo1 = mid1
                hi2 = mid2
        else:  # elif +1 == res:
            lo1 = mid1
            lo2 = mid2
    print('!', hi1 if 1 == hi1 - lo1 else hi2, flush = True)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
