from collections import *


def main() -> None:
    n, c = map(int, input().split())
    nums = map(int, input().split())

    ans = 0
    nums_cnter = Counter(nums)
    for num, cnt in nums_cnter.items():
        ans += cnt * nums_cnter[num + c]
    print(ans)


if __name__ == '__main__':
    main()
