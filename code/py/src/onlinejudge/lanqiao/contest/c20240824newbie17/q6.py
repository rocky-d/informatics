from math import comb, isqrt


def qmi(a, k, p):
    res = 1
    while k:
        if k & 1:
            res = res * a % p
        a = a * a % p
        k >>= 1
    return res


def C(a, b, p):
    if b > a:
        return 0
    res = 1
    i = 1
    j = a
    while i <= b:
        res = res * j % p
        res = res * qmi(i, p - 2, p) % p
        i += 1
        j -= 1
    return res


def lucas(a, b, p):
    if a < p and b < p:
        return C(a, b, p)
    return C(a % p, b % p, p) * lucas(a // p, b // p, p) % p


def main() -> None:
    n, m = map(int, input().split())

    ans = 0
    m_factors = 0
    num_isqrt = isqrt(m)
    for factor in range(1, num_isqrt):
        if 0 == m % factor:
            m_factors += 2
    if 0 == m % num_isqrt:
        m_factors += 1
        if m // num_isqrt != num_isqrt:
            m_factors += 1
    m_factors -= 2
    print(m_factors)
    for i in range(1, n + 1):
        j = n - i
        ans += (
            (lucas(n, i, 998244353) % 998244353)
            * (lucas(m_factors + j, j, 998244353) % 998244353)
            % 998244353
        )
        ans %= 998244353
    print(ans)


if __name__ == '__main__':
    main()
