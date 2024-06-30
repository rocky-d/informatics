from rockyutil.leetcode import *


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        @cache
        def dfs(idx: int, val: int) -> int:
            if n == idx:
                return 1 if target == val else 0
            num, cnt = nums[idx], 0
            for i in range(idx, n):
                if num == nums[i]:
                    cnt += 1
                else:
                    idx = i
                    break
            else:
                idx = n
            return (0b1 << cnt) * dfs(idx, val) if 0 == num else sum(comb(cnt, i) * dfs(idx, nxt) for i, nxt in enumerate(range(val - cnt * num, val + cnt * num + 1, num + num)))

        return dfs(idx = 0, val = 0)
