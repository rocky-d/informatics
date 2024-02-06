from math import isqrt


def is_prime_optimized(n: int) -> bool:
    if n < 2:
        res = False
    else:
        for i in range(2, isqrt(n) + 1):
            if 0 == n % i:
                res = False
                break
        else:
            res = True
    return res


def main() -> None:
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(input()))

    for num in nums:
        print('Yes' if is_prime_optimized(num) else 'No')


if __name__ == '__main__':
    main()
