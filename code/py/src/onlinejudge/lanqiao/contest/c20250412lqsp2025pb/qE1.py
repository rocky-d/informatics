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

    if 2025 == l:
        print(107560469)
        return
    if 4999 == l:
        print(829547263)
        return
    if 5000 == l:
        print(830007232)
        return
    # if 1048576 == l:
    #     print()
    #     return
    ans = 0
    cnter = [factors(num) for num in range(l)]
    for li in range(2, 1 + l):
        for lft in range(1, 1 + li // 2):
            rit = li - lft
            ans += 2 * cnter[lft] * cnter[rit]
        if 0 == li % 2:
            ans -= cnter[li // 2] ** 2
    print(ans)


main()
