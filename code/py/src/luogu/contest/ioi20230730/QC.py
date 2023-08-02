def combinationSum2(nums, target):
    nums.sort()  # 首先对数组进行排序，方便后面的去重处理
    res = []  # 用于存储符合条件的组合

    def backtrack(start, target, path):
        if target == 0:  # 如果目标数为0，说明找到了一个符合条件的组合
            res.append(path)
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:  # 去除重复的情况
                continue
            if target < nums[i]:  # 剪枝：如果当前数字大于目标数，后面的数字肯定也大于，直接结束循环
                break
            # 递归搜索下一层
            backtrack(i + 1, target - nums[i], path + [nums[i]])

    backtrack(0, target, [])
    return len(res)

# 读取输入
n, target = map(int, input().split())
nums = list(map(int, input().split()))

# 调用函数并输出结果
print(combinationSum2(nums, target))
