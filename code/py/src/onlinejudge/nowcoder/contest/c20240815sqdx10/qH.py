from math import gcd


def extended_gcd(a, b):
    """Extended Euclidean Algorithm to find the inverse of a modulo b."""
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)


def mod_inverse(a, m):
    """Calculate the modular multiplicative inverse of a modulo m."""
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m


def solve_congruence(x, y, P = 998244353):
    """Solve the congruence equation xz ≡ y (mod P)."""
    # Find the modular inverse of x modulo P
    z_inv = mod_inverse(x, P)

    # Calculate z
    z = (y * z_inv) % P

    return z


def solve(x, y, p = 998244353):
    return (y * pow(x, p - 2, p)) % p


p = 998244353


def main() -> None:
    a, b = map(int, input().split())

    total = a + b
    if 1 == bin(total)[2:].count('1'):
        g1, g2 = gcd(a, total), gcd(b, total)
        print(solve_congruence(total // g1, a // g1), solve_congruence(total // g2, b // g2))
    else:
        g1, g2 = gcd(a, total), gcd(b, total)
        print(solve_congruence(total // g1, a // g1), solve_congruence(total // g2, b // g2))


if __name__ == '__main__':
    main()
