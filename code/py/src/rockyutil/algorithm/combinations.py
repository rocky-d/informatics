from math import comb


def combinations(n, k, mod = None):
    c = [0] * (1 + k)
    c[0] = 1
    for i in range(1 + n):
        for j in range(min(i, k), 0, -1):
            c[j] += c[j - 1]
            if mod is not None:
                c[j] %= mod
    return c[-1]


if __name__ == '__main__':
    print(combinations(100, 24, 10007))
    print(comb(100, 24) % 10007)
