from math import ceil

a, b = 2, 5
print((a + b) // 2 == (a - b) // 2 + b)

x, n = 10, 3
print((x + n - 1) // n == ceil(x / n))
