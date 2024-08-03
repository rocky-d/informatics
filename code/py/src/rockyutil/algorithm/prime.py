from math import isqrt


def is_prime_plain(num):
    return 2 <= num and all(0 != num % divisor for divisor in range(2, num))


def is_prime_optimized(num):
    return 2 <= num and all(0 != num % divisor for divisor in range(2, isqrt(num) + 1))


def primes_before_eratosthenes(n):
    tags = [False] * 2 + [True] * n  # tags = [False] * min(2, n) + [True] * max(0, n - 2)
    for num in range(2, n):
        if tags[num]:
            yield num
            for composite in range(num * num, n, num):
                tags[composite] = False


def primes_before_euler(n):
    primes = []
    tags = [False] * 2 + [True] * n  # tags = [False] * min(2, n) + [True] * max(0, n - 2)
    for num in range(2, n):
        if tags[num]:
            yield num
            primes.append(num)
        for prime in primes:
            composite = num * prime
            if composite < n:
                tags[composite] = False
                if 0 == num % prime:
                    break
            else:
                break


if __name__ == '__main__':
    from timeit import timeit

    n, repeats = 10 ** 7, 10 ** 1
    match 3:
        case 1:
            print(timeit(lambda: tuple(filter(is_prime_plain, range(n))), number = repeats))
        case 2:
            print(timeit(lambda: tuple(filter(is_prime_optimized, range(n))), number = repeats))
        case 3:
            print(timeit(lambda: tuple(primes_before_eratosthenes(n)), number = repeats))
        case 4:
            print(timeit(lambda: tuple(primes_before_euler(n)), number = repeats))
