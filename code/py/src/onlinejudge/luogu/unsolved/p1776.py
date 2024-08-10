def main():
    n, w = map(int, input().split())

    dp = [0 for _ in range(1 + w)]

    for _ in range(n):
        vv, ww, mm = map(int, input().split())
        count = 1
        while mm > count:
            mm -= count
            vvv = vv * count
            www = ww * count
            for j in range(w, www - 1, -1):
                dp[j] = max(dp[j], dp[j - www] + vvv)
            count <<= 1
        vvv = vv * mm
        www = ww * mm
        for j in range(w, www - 1, -1):
            dp[j] = max(dp[j], dp[j - www] + vvv)

    print(dp[w])


if __name__ == '__main__':
    main()
