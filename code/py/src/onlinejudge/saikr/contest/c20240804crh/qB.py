from collections import deque
from math import isqrt, ceil


def main() -> None:
    n = int(input())

    ans = []

    def is_prime(num):
        return 2 <= num and all(0 != num % i for i in range(2, isqrt(num) + 1))

    digits = deque()

    def dfs(i):
        if i == 0:
            if 0b0 == 0b1 & n:
                num = int(''.join(digits) + ''.join(reversed(digits)))
            else:
                num = int(''.join(digits)[:-1] + ''.join(reversed(digits)))
            if is_prime(num):
                ans.append(num)
            return
        i -= 1
        for digit in '0123456789':
            digits.append(digit)
            dfs(i)
            digits.pop()

    dfs(ceil(n / 2))
    print(len(ans))
    print(*ans)


if __name__ == '__main__':
    main()
