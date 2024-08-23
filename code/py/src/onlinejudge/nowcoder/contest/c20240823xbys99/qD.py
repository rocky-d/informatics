def main() -> None:
    n = int(input())
    a = map(int, input().split())

    a = sorted(a)

    def check(mid: int) -> bool:
        for ai in a:
            x, y = divmod(mid, ai)
            if 0 == y:
                return True


    lo, hi = 1, 10_000_000_001
    while 1 < hi - lo:
        mid = lo + hi >> 1
        if check(mid=mid):
            lo = mid
        else:
            hi = mid
    print(hi)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
