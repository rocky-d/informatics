from itertools import accumulate


def main() -> None:
    t = map(int, input().split())

    ans = 0
    t = list(t)
    prefs = [0] + list(accumulate(t))
    for leng in range(1, 1 + len(t)):
        cum = 0
        cnt = 0
        for i in range(leng):
            cum += prefs[i]
            cnt = prefs[i + 1]
            if 100 <= cnt:
                break
        ans = max(ans, min(100, cnt) - cum)
    print(ans)


main()
