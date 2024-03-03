from math import isqrt


def primefactors(num):
    ans = []
    for factor in range(2, isqrt(num) + 1):
        times = 0
        while 0 == num % factor:
            num //= factor
            times += 1
        if 0 < times:
            ans.append((factor, times))
    if 1 < num:
        ans.append((num, 1))
    return ans


if __name__ == '__main__':
    print(*primefactors(10 ** 12), sep = '\n')
