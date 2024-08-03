from bisect import bisect_left


def main() -> None:
    n, k = map(int, input().split())
    a = map(int, input().split())
    b = map(int, input().split())

    ans = 0
    a, b = list(a), list(b)
    least = max(0, bisect_left(range(max(a) + 1), -k, lo = 0, key = lambda mid: -sum(max(0, (ai - mid) // bi + 1) for ai, bi in zip(a, b))) - 1)
    cnt = 0
    for ai, bi in zip(a, b):
        tmp = max(0, (ai - least) // bi + 1)
        ans += (ai + ai - (tmp - 1) * bi) * tmp // 2
        cnt += tmp
    ans -= (cnt - k) * least
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
