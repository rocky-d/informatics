def check(mid: int) -> bool:
    print('?', mid, mid, flush = True)
    return mid * mid == int(input())


def main() -> None:
    lo, hi = 1, 1000
    while 1 < hi - lo:
        mid = hi + lo >> 1
        if check(mid = mid):
            lo = mid
        else:
            hi = mid
    print('!', hi, flush = True)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
