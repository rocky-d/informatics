class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        res = len_nums = len(nums)
        j = len_nums - 1
        for i in range(len_nums):
            if nums[i] == val:
                while -1 < j and nums[j] == val:
                    j -= 1
                if j < i:
                    res = i
                    break
                else:
                    nums[i], nums[j] = nums[j], nums[i]
        return res


ls = [3, 2, 2, 3]
Solution.removeElement(..., ls, 3)
print(ls)
