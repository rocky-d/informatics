from itertools import accumulate
from operator import mul

mod = 1_000_000_007


def inverse(x):
    return pow(x, mod - 2, mod) % mod


def main() -> None:
    n, k = map(int, input().split())
    a = input().split()

    ans = 0
    cnt0 = a.count('0')
    cnt1 = n - cnt0
    prefs = list(pref % mod for pref in accumulate(range(1, 1 + n), func = mul, initial = 1))
    for i in range(k + 1 >> 1, k + 1):
        ans += (prefs[cnt1] * inverse(prefs[i]) * inverse(prefs[cnt1 - i])) * (
                prefs[cnt0] * inverse(prefs[k - i]) * inverse(prefs[cnt0 - (k - i)])) % mod
        ans %= mod
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
