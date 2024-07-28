def main() -> None:
    n, m = map(int, input().split())
    matches = [list(map(int, input().split())) for _ in range(n)]
    target = int(input())

    total = 5001
    dp = [False] * total
    for num in matches.pop(0):
        dp[num] = True
    for match in matches:
        dp_lst, dp = dp, [False] * total
        for i in range(total):
            if dp_lst[i]:
                for num in match:
                    num += i
                    if num < total:
                        dp[num] = True
    print(min(abs(target - i) for i in range(total) if dp[i]))


if __name__ == '__main__':
    main()
