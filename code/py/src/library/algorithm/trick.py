from math import ceil, floor

if __name__ == '__main__':
    a, b = 2, 5
    print(floor((b - a) / 2) == (b - a) // 2)
    print(floor((a - b) / 2) == (a - b) // 2)
    print(floor((b - a) / 2) == int((b - a) / 2))
    print(ceil((a - b) / 2) == int((a - b) / 2))

    x, n = 10, 3
    print(ceil(x / n) == (x + n - 1) // n)
