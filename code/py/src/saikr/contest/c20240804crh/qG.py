from math import ceil


def main() -> None:
    a, b, c = map(int, input().split())

    if 1 + a != c:
        print(-1)
        return
    ab = a + b
    lo, hi = -1, ab + 1
    while 1 < hi - lo:
        mid = lo + hi >> 1
        if (1 << mid) - 1 <= a:
            lo = mid
        else:
            hi = mid
    cnt = hi - 1

    a_lst = a - (2 ** cnt - 1)
    if 0 < a_lst:
        free = 2 ** cnt - a_lst
        b -= free
        if b <= 0:
            print(cnt + 1)
            return
        free = a_lst + 2 ** cnt
        print(cnt + 1 + ceil(b / free))
    else:
        free = 2 ** cnt
        print(cnt + ceil(b / free))


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
