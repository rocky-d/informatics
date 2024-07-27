from math import ceil, floor

a, b = 2, 5
print((b - a) // 2 == floor((b - a) / 2))
print((a - b) // 2 == floor((a - b) / 2))
print(int((b - a) / 2) == floor((b - a) / 2))
print(int((a - b) / 2) == ceil((a - b) / 2))
print((a + b) // 2 == (a - b) // 2 + b)

x, n = 10, 3
print((x + n - 1) // n == ceil(x / n))
