def main() -> None:
    n = int(input())
    nums = list(map(int, input().split()))

    tree = [0 for _ in range(n)]
    p = 0

    def fill(index: int) -> None:
        if n < index:
            return
        nonlocal p
        fill(2 * index)
        fill(2 * index + 1)
        tree[index - 1] = nums[p]
        p += 1

    fill(1)
    print(*tree)


if __name__ == '__main__':
    main()
