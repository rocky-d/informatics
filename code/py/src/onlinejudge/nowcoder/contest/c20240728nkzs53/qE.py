from collections import Counter


def main() -> None:
    n = int(input())
    a = map(int, input().split())

    cnter_a = Counter()
    for ai in a:
        while 0 < ai:
            cnter_a[ai] += 1
            ai >>= 1
        cnter_a[ai] += 1
    lo, hi = 0, n + 1
    while 1 < hi - lo:
        mid = lo + hi >> 1
        cnter = Counter()
        for num in range(mid):
            while 0 < num:
                cnter[num] += 1
                num >>= 1
            cnter[num] += 1
        if all(cnt <= cnter_a[num] for num, cnt in cnter.items()):
            lo = mid
        else:
            hi = mid
    print(lo)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
