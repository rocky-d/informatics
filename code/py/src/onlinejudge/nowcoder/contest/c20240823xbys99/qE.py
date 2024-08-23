from bisect import bisect_right
from itertools import groupby
from math import inf


def main() -> None:
    n, m = map(int, input().split())
    h = map(int, input().split())
    x = map(int, input().split())

    xh = sorted(zip(x, h), key=lambda item: item[0])
    dp = list(range(n))
    for i in reversed(range(n - 1)):
        idx = bisect_right(xh, (xh[i][0] + xh[i][1], inf)) - 1
        val = dp[idx]
        for j in range(i, idx):
            dp[j] = val
    print(sum(sorted((len(list(group)) for _, group in groupby(dp)), reverse=True)[:m]))


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
