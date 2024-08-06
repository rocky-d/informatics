from collections import Counter


def main() -> None:
    n, c = map(int, input().split())
    nums = map(int, input().split())

    cnter = Counter(nums)
    print(sum(cnter[num + c] * cnt for num, cnt in cnter.items()))


if __name__ == '__main__':
    main()
