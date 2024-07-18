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
    prefs_x_idxes, prefs_y_idxes = {}, {}
    for idx, val in enumerate(prefs_x):
        if val not in prefs_x_idxes.keys():
            prefs_x_idxes[val] = []
        prefs_x_idxes[val].append(idx)
    for idx, val in enumerate(prefs_y):
        if val not in prefs_y_idxes.keys():
            prefs_y_idxes[val] = []
        prefs_y_idxes[val].append(idx)
    for i in range(1, n + 1):
        diff_x, diff_y = prefs_x[i] - x, prefs_y[i] - y
        if diff_x in prefs_x_idxes.keys() and diff_y in prefs_y_idxes.keys():
            ans += (n + 1 - i) * len({idx for idx in prefs_x_idxes[diff_x] if idx < i} & {idx for idx in prefs_y_idxes[diff_y] if idx < i})
    print(ans)


if __name__ == '__main__':
    main()
