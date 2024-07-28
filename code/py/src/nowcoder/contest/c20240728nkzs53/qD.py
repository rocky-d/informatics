def main() -> None:
    n, m = map(int, input().split())
    matches = [map(int, input().split()) for _ in range(n)]
    target = int(input())

    dp = {0}
    for match in matches:
        match = list(match)
        dp_lst, dp = dp, set()
        for lst in dp_lst:
            for num in match:
                dp.add(lst + num)
    print(min(abs(target - num) for num in dp))


if __name__ == '__main__':
    main()
