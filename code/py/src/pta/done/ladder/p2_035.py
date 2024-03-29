def main() -> None:
    n = int(input())
    nums = map(int, input().split())

    tree = [0 for _ in range(n)]

    def dfs(index: int) -> None:
        if n <= index:
            return
        dfs(index = 2 * index + 1)
        dfs(index = 2 * index + 2)
        tree[index] = next(nums)

    dfs(index = 0)
    print(*tree)


if __name__ == '__main__':
    main()
