from bisect import bisect


def main() -> None:
    n = int(input())
    a = map(int, input().split())

    a = list(a)
    odd, eves = -1, []
    for ai in a:
        if 0b1 == 0b1 & ai:
            odd = max(odd, ai)
        else:
            eves.append(ai)
    if 0 == len(eves) or n == len(eves):
        print(0)
        return
    eves.sort()
    eves_len = len(eves)
    lo = 0
    while True:
        idx = bisect(eves, odd, lo = lo)
        if idx == eves_len:
            extra = 0
            break
        if idx == lo:
            extra = 1
            break
        odd += sum(eves[i] for i in range(lo, idx))
        lo = idx
    print(eves_len + extra)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
