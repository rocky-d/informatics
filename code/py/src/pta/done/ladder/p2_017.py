def main() -> None:
    n = int(input())
    nums = map(int, input().split())

    nums_sorted = sorted(nums)
    pivot = n // 2
    print(f"Outgoing #: {n - pivot}")
    print(f"Introverted #: {pivot}")
    print(f"Diff = {sum(nums_sorted[pivot:]) - sum(nums_sorted[:pivot])}")


if __name__ == '__main__':
    main()
