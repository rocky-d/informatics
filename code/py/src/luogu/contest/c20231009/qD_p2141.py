def main() -> None:
    ans = 0
    input()
    nums = sorted(map(int, input().split()))
    nums_set = set(nums)
    for i, numi in enumerate(nums):
        for j in range(i):
            diff = numi - nums[j]
            if diff != nums[j] and diff in nums_set:
                ans += 1
                break
    print(ans)


if __name__ == '__main__':
    main()
