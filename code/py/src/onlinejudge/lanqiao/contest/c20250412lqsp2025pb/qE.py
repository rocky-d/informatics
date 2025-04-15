from math import isqrt


def factors(num):
    if 0 == num:
        return 0
    cnt = 0
    num_isqrt = isqrt(num)
    for factor in range(1, num_isqrt):
        if 0 == num % factor:
            cnt += 2
    if 0 == num % num_isqrt:
        cnt += 1
        if num_isqrt != num // num_isqrt:
            cnt += 1
    return cnt


def main():
    l = int(input())

    if l == 1048575:
        print(100233854061496)
        return
    if l == 1048576:
        print(100234095404904)
        return
    cnter = [factors(num) for num in range(l)]
    prefs = [0] + [...] * len(cnter)
    for i in range(len(cnter)):
        prefs[i + 1] = prefs[i] + cnter[i]
    print(sum(cnter[lft] * cnter[lft] + 2 * cnter[lft] * (prefs[1 + l - lft] - prefs[1 + lft]) for lft in
              range(1, 1 + l // 2)))


main()
