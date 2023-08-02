# 百分比
n = int(input())
array = list(map(int, input().split()))
array.sort()
k1 = (n - 1) * (15 / 100)
i1 = int(k1)
j1 = ((n - 1) * (15 / 100)) - i1

k2 = (n - 1) * (35 / 100)
i2 = int(k2)
j2 = ((n - 1) * (35 / 100)) - i2

k3 = (n - 1) * (55 / 100)
i3 = int(k3)
j3 = ((n - 1) * (55 / 100)) - i3

k4 = (n - 1) * (75 / 100)
i4 = int(k4)
j4 = ((n - 1) * (75 / 100)) - i4

w1 = (1 - j1) * array[i1] + j1 * array[i1 + 1]
w2 = (1 - j2) * array[i2] + j2 * array[i2 + 1]
w3 = (1 - j3) * array[i3] + j3 * array[i3 + 1]
w4 = (1 - j4) * array[i4] + j4 * array[i4 + 1]
w1 = round(w1, 1)
w2 = round(w2, 1)
w3 = round(w3, 1)
w4 = round(w4, 1)
print('{:.2f}'.format(w1))
print('{:.2f}'.format(w2))
print('{:.2f}'.format(w3))
print('{:.2f}'.format(w4))

n = int(input())
array = list(map(int, input().split()))

array.sort()  # 对数组进行排序

percentiles = [15, 35, 55, 75]  # 给定的百分位数

for p in percentiles:
    i = int((n - 1) * (p / 100))
    j = (n - 1) * (p / 100) - i
    percentile = (1 - j) * array[i] + j * array[i + 1]
    print('{:.2f}'.format(percentile))
