from collections import Counter
from math import comb

mod = 1_000_000_007


def main() -> None:
    n, k = map(int, input().split())
    a = input().split()

    ans = 0
    cnter = Counter(a)
    cnt0, cnt1 = cnter['0'], cnter['1']
    for i in range((k >> 1) + 1, k + 1):
        ans += comb(cnt1, i) * comb(cnt0, k - i) % mod
        ans %= mod
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
