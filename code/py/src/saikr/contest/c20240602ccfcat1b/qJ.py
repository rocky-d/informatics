from math import comb


def main() -> None:
    ans = []
    for _ in range(int(input())):
        n = int(input())
        money = 2 * n - 1
        base = n + n - 2
        n_1 = n - 1
        limit = n // 2
        limit1 = limit + 1

        res = comb(base, n_1)
        print(f"{limit1 = }")
        minus = True
        for i in range(1, n + 1):
            print(f"{i = }")
            print(f"{base - i * limit1 = }")
            if minus:
                res -= comb(n, i) * comb(max(0, base - i * limit1), max(0, n_1 - i))
            else:
                res += comb(n, i) * comb(max(0, base - i * limit1), max(0, n_1 - i))
            minus = not minus
        print(f"{res = }")
        ans.append(res)
    # print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
