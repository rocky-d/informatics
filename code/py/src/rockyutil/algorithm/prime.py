from math import isqrt


def is_prime_plain(num):
    return 2 <= num and all(0 != num % divisor for divisor in range(2, num))


def is_prime_optimized(num):
    return 2 <= num and all(0 != num % divisor for divisor in range(2, isqrt(num) + 1))


def primes_before_eratosthenes(n):
    is_prime = [False] * min(2, n) + [True] * max(0, n - 2)
    for num in range(2, n):
        if is_prime[num]:
            yield num
            for composite in range(num * num, n, num):
                is_prime[composite] = False


def primes_before_euler(n):
    primes = []
    is_prime = [False] * min(2, n) + [True] * max(0, n - 2)
    for num in range(2, n):
        if is_prime[num]:
            yield num
            primes.append(num)
        for prime in primes:
            composite = num * prime
            if composite < n:
                is_prime[composite] = False
                if 0 == num % prime:
                    break
            else:
                break


if __name__ == '__main__':
    from timeit import timeit

    eg_n, repeats = 10 ** 7, 10 ** 1
    which = 3
    match which:
        case 1:
            print(timeit(lambda: tuple(filter(is_prime_plain, range(eg_n))), number = repeats))
        case 2:
            print(timeit(lambda: tuple(filter(is_prime_optimized, range(eg_n))), number = repeats))
        case 3:
            print(timeit(lambda: tuple(primes_before_eratosthenes(n = eg_n)), number = repeats))
        case 4:
            print(timeit(lambda: tuple(primes_before_euler(n = eg_n)), number = repeats))
