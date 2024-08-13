from math import isqrt, sqrt, ceil


def main() -> None:
    n = int(input())
    l, r = input().split()

    half = n >> 1
    a, b, c, d = int(l[:half]), int(l[half:]), int(r[:half]), int(r[half:])
    if a == c:  # 143500 143543
        a_isqrt = isqrt(a)
        if a == a_isqrt * a_isqrt:
            b_isqrt, d_isqrt = ceil(sqrt(b)), isqrt(d)
            cnt = d_isqrt - b_isqrt + 1
            print(cnt)
        else:
            print(0)
    elif a + 1 == c:  # 143500 144243
        cnt = 0
        a_isqrt = isqrt(a)
        if a == a_isqrt * a_isqrt:
            b_isqrt, d_isqrt = ceil(sqrt(b)), isqrt(int('9' * half))
            cnt += d_isqrt - b_isqrt + 1
        c_isqrt = isqrt(c)
        if c == c_isqrt * c_isqrt:
            b_isqrt, d_isqrt = ceil(sqrt(int('0' * half))), isqrt(d)
            cnt += d_isqrt - b_isqrt + 1
        print(cnt)
    else:  # 143500 146443
        cnt = 0
        a_isqrt = isqrt(a)
        if a == a_isqrt * a_isqrt:
            b_isqrt, d_isqrt = ceil(sqrt(b)), isqrt(int('9' * half))
            cnt += d_isqrt - b_isqrt + 1
        c_isqrt = isqrt(c)
        if c == c_isqrt * c_isqrt:
            b_isqrt, d_isqrt = ceil(sqrt(int('0' * half))), isqrt(d)
            cnt += d_isqrt - b_isqrt + 1
        lft = isqrt(c - 1) - ceil(sqrt(a + 1)) + 1
        rit = isqrt(int('9' * half)) - ceil(sqrt(int('0' * half))) + 1
        cnt += lft * rit
        print(cnt)


if __name__ == '__main__':
    main()
