from math import log2, comb

mod = 998244353


def main() -> None:
    l, r = map(int, input().split())

    l_1 = l - 1
    x = int(log2(r // l))
    base = 0b1 << x
    cnt = (r // base - l_1) % mod
    for i in range(1, 1 + x):
        base = 3 * (base >> 1)
        n = r // base - l_1
        if n <= 0:
            break
        cnt += n * comb(x, i)
        cnt %= mod
    print(1 + x, cnt)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
