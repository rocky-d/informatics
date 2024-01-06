from random import randint
from threading import Thread


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def filter_primes(nums):
    return [is_prime(num) for num in nums]


if __name__ == "__main__":
    nums = [randint(100, 10000) for i in range(2000)]

    threads = [
        Thread(target = filter_primes, args = (nums,)),
        Thread(target = filter_primes, args = (nums,)),
        Thread(target = filter_primes, args = (nums,))
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
