# 1 2 3 4 5 6 7 8 9

# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# ...
# 90 91 92 93 94 95 96 97 98 99

# 100 101 102 103 104 105 106 107 108 109
# 110 111 112 113 114 115 116 117 118 119
# 120 121 122 123 124 125 126 127 128 129
# ...
# 990 991 992 993 994 995 996 997 998 999

# 1000


def main():
    res = 0
    n, x = map(int, input().split())
    m = 1
    while m <= n:
        a = n // (m * 10)
        b = (n // m) % 10
        c = n % m
        if x:
            if b > x:
                res += (a + 1) * m
            if b == x:
                res += a * m + c + 1
            if b < x:
                res += a * m
        else:
            if b:
                res += a * m
            else:
                res += (a - 1) * m + c + 1
        m *= 10
    print(res)


# def main():
#     n, x = input().split()
#     print(str([i for i in range(int(n), 0, -1)]).count(x))


if __name__ == '__main__':
    main()
