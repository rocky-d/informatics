from array import array


def main():
    n, m, q = map(int, input().split())

    ans = 0
    m -= 1
    pow2 = array('I', [1])
    for _ in range(m * (n - 1)):
        pow2.append((pow2[-1] << 1) % q)
    combn = [1]
    for i in range(1, n + 1):
        combni = combn[-1] * (n - i + 1) // i
        combn.append(combni)
        ans += (combni % q) * pow2[m * (n - i)] * pow(pow2[i] - 1, m, q) % q
        ans %= q
    print(ans)


if __name__ == '__main__':
    main()
