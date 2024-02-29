def main() -> None:
    n, m = map(int, input().split())
    matrix = tuple(input() for _ in range(n))

    ans = 0
    for row in range(1, n - 1):
        for col in range(1, m - 1):
            char = matrix[row][col]
            cnt = 1
            while cnt <= row < n - cnt and cnt <= col < m - cnt and char == matrix[row - cnt][col - cnt] == matrix[row - cnt][col + cnt] == matrix[row + cnt][col]:
                cnt += 1
            ans = max(ans, cnt - 1)
    print(ans)


if __name__ == '__main__':
    main()
