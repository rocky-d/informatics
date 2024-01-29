def main() -> None:
    n = int(input())
    nums = map(int, input().split())

    tree = [0 for _ in range(n)]

    def fill(index: int) -> None:
        if n <= index:
            return
        fill(2 * index + 1)
        fill(2 * index + 2)
        tree[index] = next(nums)

    fill(0)
    print(*tree)


if __name__ == '__main__':
    main()
