from math import isqrt


def is_prime_optimized(num: int) -> bool:
    if num < 2:
        res = False
    else:
        for i in range(2, isqrt(num) + 1):
            if 0 == num % i:
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
        print('Yes' if is_prime_optimized(num = num) else 'No')


if __name__ == '__main__':
    main()
