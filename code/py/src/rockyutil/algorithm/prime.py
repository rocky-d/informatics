from math import isqrt


def is_prime_plain(num):
    return all(num % divisor for divisor in range(2, num))


def is_prime_optimized(num):
    return all(num % divisor for divisor in range(2, isqrt(num) + 1))


def primes_before_eratosthenes(n):
    tags = [False for _ in range(min(2, n))] + [True for _ in range(2, n)]
    for num in range(2, n):
        if tags[num]:
            yield num
            for composite in range(num * num, n, num):
                tags[composite] = False


def primes_before_euler(n):
    primes = []
    tags = [False for _ in range(min(2, n))] + [True for _ in range(2, n)]
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

    eg_n, repeats = int(1e7), int(1e1)
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
