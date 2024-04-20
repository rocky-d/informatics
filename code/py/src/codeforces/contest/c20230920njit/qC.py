def main() -> None:
    tests = int(input())
    while tests > 0:
        tests -= 1
        input()
        nums = list(map(int, input().split()))
        sorted_nums = sorted(nums)
        max_ = sorted_nums[-1]
        max_index = nums.index(max_)
        res = []
        for i in range(len(nums)):
            if i == max_index:
                res.append(nums[i] - sorted_nums[-2])
            else:
                res.append(nums[i] - max_)
        print(*res)


if __name__ == '__main__':
    main()
