from decimal import Decimal


def main() -> None:
    n = int(input())
    a = (map(int, input().split()) for _ in range(n))

    ans = Decimal('0.0')
    a = [tuple(ai) for ai in a]
    for i in range(n):
        j = (i + 1) % n
        dx, dy = a[i][0] - a[j][0], a[i][1] - a[j][1]
        ans += Decimal(str(dx * dx + dy * dy)).sqrt()

    m = int(input())
    b = (map(int, input().split()) for _ in range(m))

    dst2 = 0
    m_half = m >> 1
    b = [tuple(bi) for bi in b]
    if 0b0 == 0b1 & m:
        for i in range(3 + m_half):
            i %= m
            tmp = i + m_half
            for j in range(tmp - 1, tmp + 2):
                j %= m
                dx, dy = b[i][0] - b[j][0], b[i][1] - b[j][1]
                dst2 = max(dst2, dx * dx + dy * dy)
    else:
        for i in range(3 + m_half):
            i %= m
            tmp = i + m_half
            for j in range(tmp - 1, tmp + 3):
                j %= m
                dx, dy = b[i][0] - b[j][0], b[i][1] - b[j][1]
                dst2 = max(dst2, dx * dx + dy * dy)
    ans = ans + Decimal(str(dst2)).sqrt() * Decimal('6.28318530717958647692')
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
