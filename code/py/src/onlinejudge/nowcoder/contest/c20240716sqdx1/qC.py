def main() -> None:
    q = int(input())
    tv = (map(int, input().split()) for _ in range(q))

    ans = []
    a_len = 0
    prefs = [0] * 500_001
    for t, v in tv:
        a_len -= t - 1
        prefs[a_len] = (prefs[a_len - 1] + a_len * v) % 1_000_000_007
        ans.append(prefs[a_len])
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
