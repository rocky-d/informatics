from itertools import pairwise

mod = 1_000_000_007

c = [[1] + [0] * (i + 1) for i in range(200_000)]
for i, (c_lst, c_nxt) in enumerate(pairwise(c), start = 1):
    for j in range(i, 0, -1):
        c_nxt[j] = c_lst[j - 1] + c_lst[j]
        if mod is not None:
            c_nxt[j] %= mod


def main() -> None:
    n, k = map(int, input().split())
    a = map(int, input().split())

    ans = 0
    a = list(a)
    half = k // 2
    for i in range(half, n - half):
        if 0 == a[i]:
            continue
        ans += (c[i][half] + c[n - i - 1][half]) % mod
        ans %= mod
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
