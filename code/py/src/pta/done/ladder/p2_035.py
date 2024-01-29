def main() -> None:
    n = int(input())
    nums = map(int, input().split())

    tree = [0 for _ in range(n)]

    def fill(index: int) -> None:
        if n < index:
            return
        fill(2 * index)
        fill(2 * index + 1)
        tree[index - 1] = next(nums)

    fill(1)
    print(*tree)


if __name__ == '__main__':
    main()
