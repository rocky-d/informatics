from math import comb

mod = 1_000_000_007


def main() -> None:
    n, m = map(int, input().split())

    ans = 0
    for base in range(n - 2, m):
        for lft in range(n - 2):
            rit = n - 3 - lft
            ans += base * comb(base - 1, lft) * comb(base - 1 - lft, rit)
            ans %= mod
    print(ans)


if __name__ == '__main__':
    main()
