def main() -> None:
    n, k = map(int, input().split())
    matrix = (input() for _ in range(n))

    ans = []
    matrix = list(matrix)
    for i in range(0, n, k):
        line, row = '', matrix[i]
        for j in range(0, n, k):
            line += row[j]
        ans.append(line)
    print(*ans, sep = '\n')


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
