from collections import Counter


def main() -> None:
    n, c = map(int, input().split())
    nums = map(int, input().split())

    nums = list(nums)
    cnter = Counter(nums)
    print(sum(cnter[c + num] for num in nums))


if __name__ == '__main__':
    main()
