from bisect import bisect_right


def main() -> None:
    n, k = map(int, input().split())
    a = map(int, input().split())
    b = map(int, input().split())

    ans = 0
    a, b = list(a), list(b)
    lst = max(0, bisect_right(range(max(a) + 1), -k, lo = 0, key = lambda mid: -sum((ai - mid) // bi + 1 for ai, bi in zip(a, b) if mid <= ai)) - 1)
    for ai, bi in zip(a, b):
        if lst <= ai:
            cnt = (ai - lst) // bi + 1
            k -= cnt
            ans += cnt * (ai + ai - bi * (cnt - 1)) // 2
    ans += k * lst
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
