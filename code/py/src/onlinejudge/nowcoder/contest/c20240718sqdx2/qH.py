from bisect import bisect_left


def main() -> None:
    n, x, y = map(int, input().split())
    s = input()

    if n < abs(x) + abs(y):
        print(0)
        return
    if n == abs(x) + abs(y):
        print(1)
        return
    if 0 == x == y:
        print((1 + n) * n // 2)
        return
    ans = 0
    prefs_x, prefs_y = [0] + [0] * n, [0] + [0] * n
    for i, char in enumerate(s, start = 1):
        if 'W' == char:
            prefs_x[i] = prefs_x[i - 1]
            prefs_y[i] = prefs_y[i - 1] + 1
        elif 'S' == char:
            prefs_x[i] = prefs_x[i - 1]
            prefs_y[i] = prefs_y[i - 1] - 1
        elif 'A' == char:
            prefs_x[i] = prefs_x[i - 1] - 1
            prefs_y[i] = prefs_y[i - 1]
        else:  # elif 'D' == char:
            prefs_x[i] = prefs_x[i - 1] + 1
            prefs_y[i] = prefs_y[i - 1]
    prefs_x_is, prefs_y_is = {}, {}
    for i, val in enumerate(prefs_x):
        if val not in prefs_x_is.keys():
            prefs_x_is[val] = []
        prefs_x_is[val].append(i)
    for i, val in enumerate(prefs_y):
        if val not in prefs_y_is.keys():
            prefs_y_is[val] = []
        prefs_y_is[val].append(i)
    for i in range(1, 1 + n):
        diff_x, diff_y = prefs_x[i] - x, prefs_y[i] - y
        if diff_x in prefs_x_is.keys() and diff_y in prefs_y_is.keys():
            ls_x, ls_y = prefs_x_is[diff_x], prefs_y_is[diff_y]
            ans += (n + 1 - i) * len(frozenset(ls_x[:bisect_left(ls_x, i)]) & frozenset(ls_y[:bisect_left(ls_y, i)]))
    print(ans)


if __name__ == '__main__':
    main()
