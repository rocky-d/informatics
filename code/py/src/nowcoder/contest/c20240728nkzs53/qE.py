def main() -> None:
    n = int(input())
    a = map(int, input().split())

    a = sorted(a)
    nums = [False] * n + [False]
    p = 0
    for ai in a:
        lst = ai
        while p < ai:
            lst = ai
            ai //= 2
        if ai == p:
            nums[p] = True
            while nums[p]:
                p += 1
        else:
            if lst < len(nums):
                nums[lst] = True
    print(p)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
