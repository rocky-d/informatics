def main() -> None:
    ans = 0
    input()
    nums = sorted(map(int, input().split()))
    for i, numi in enumerate(nums):
        for j in range(i):
            diff = numi - nums[j]
            if not diff == nums[j] and diff in nums:
                ans += 1
                break
    print(ans)


if __name__ == '__main__':
    main()
