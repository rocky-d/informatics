def check(mid1: int, mid2: int) -> int:
    print('?', mid1, mid2, flush = True)
    x = int(input())
    if x == mid1 * mid2:
        res = +1
    elif x == mid1 * (mid2 + 1):
        res = 0
    else:  # elif x == (mid1 + 1) * (mid2 + 1):
        res = -1
    return res


def main() -> None:
    lo, hi = 1, 1000
    diff = hi - lo
    while 1 < diff:
        mid1 = lo + diff // 3
        mid2 = lo + (diff << 1) // 3
        res = check(mid1 = mid1, mid2 = mid2)
        if +1 == res:
            lo = mid2
        elif 0 == res:
            lo = mid1
            hi = mid2
        else:  # elif -1 == res:
            hi = mid1
        diff = hi - lo
    print('!', hi, flush = True)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
