from random import randint
from threading import *


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def get_primes(nums):
    return [is_prime(num) for num in nums]


if __name__ == "__main__":
    nums_ = [randint(100, 10000) for i in range(2000)]

    thread1 = Thread(target = get_primes, args = (nums_,))
    thread2 = Thread(target = get_primes, args = (nums_,))
    thread3 = Thread(target = get_primes, args = (nums_,))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()
