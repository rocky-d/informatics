def main() -> None:
    nums = [99, 22, 51, 63, 72, 61, 20, 88, 40, 21, 63, 30, 11, 18, 99, 12, 93, 16, 7, 53, 64, 9, 28, 84, 34, 96, 52,
            82, 51, 77]
    cnt = 0
    ans = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            cnt += 1
            if 2022 <= nums[i] * nums[j]:
                ans += 1
    print(cnt)
    print(ans)


if __name__ == '__main__':
    main()
