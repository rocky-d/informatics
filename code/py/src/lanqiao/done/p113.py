def main() -> None:
    def dfs() -> int:
        res = -1
        stars = 0
        for i, item in enumerate(blocks):
            if '*' == item:
                stars += 1
                blocks[i] = 'L'
                if 2 <= i and 'L' == blocks[i - 2] and 'O' == blocks[i - 1]:
                    res = 1
                elif i <= n - 3 and 'L' == blocks[i + 2] and 'O' == blocks[i + 1]:
                    res = 1
                else:
                    res = max(res, -dfs())
                blocks[i] = '*'
                if 1 == res:
                    break

                blocks[i] = 'O'
                if 1 <= i <= n - 2 and 'L' == blocks[i - 1] == blocks[i + 1]:
                    res = 1
                else:
                    res = max(res, -dfs())
                blocks[i] = '*'
                if 1 == res:
                    break
        if 0 == stars:
            res = 0
        return res

    for _ in range(int(input())):
        blocks = list(input())
        n = len(blocks)
        print(dfs())


if __name__ == '__main__':
    main()
