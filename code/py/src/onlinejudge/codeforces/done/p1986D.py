from math import inf


def main() -> None:
    n = int(input())
    s = input()

    digits = list(map(int, s))
    if 2 == n:
        print(10 * digits[0] + 1 * digits[1])
        return
    if 3 == n:
        a, b = digits[0], 10 * digits[1] + 1 * digits[2]
        ans = min(a + b, a * b)
        a, b = 10 * digits[0] + 1 * digits[1], digits[2]
        ans = min(ans, a + b, a * b)
        print(ans)
        return
    if 0 in digits:
        print(0)
        return
    ans = inf
    for i in range(1, n):
        cnt = 0
        for num in digits[:i - 1] + [10 * digits[i - 1] + 1 * digits[i]] + digits[i + 1:]:
            if 1 == num:
                continue
            cnt += num
        ans = min(ans, cnt)
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
