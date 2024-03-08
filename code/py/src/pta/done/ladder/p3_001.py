from bisect import insort_right


def main() -> None:
    n, m = map(int, input().split())
    coins = map(int, input().split())

    dp, permutations = [0 for _ in range(1 + m)], [[] for _ in range(1 + m)]
    for coin in coins:
        for vol in range(m, coin - 1, -1):
            new_dp_val = dp[vol - coin] + coin
            if dp[vol] < new_dp_val:
                dp[vol] = new_dp_val
                permutations[vol] = permutations[vol - coin].copy()
                insort_right(permutations[vol], coin)
            elif dp[vol] == new_dp_val:
                new_permutations_val = permutations[vol - coin].copy()
                insort_right(new_permutations_val, coin)
                if new_permutations_val < permutations[vol]:
                    permutations[vol] = new_permutations_val
    if m == dp[-1]:
        ans = ' '.join(map(str, permutations[-1]))
    else:
        ans = 'No Solution'
    print(ans)


if __name__ == '__main__':
    main()
