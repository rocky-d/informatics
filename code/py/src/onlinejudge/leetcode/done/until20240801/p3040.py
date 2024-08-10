from onlinejudge.leetcode import *


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        ans, cnt = 0, 0

        @cache
        def dfs(lft: int, rit: int, score: int) -> None:
            nonlocal ans, cnt
            ans = max(ans, cnt)
            if rit <= lft:
                return
            cnt += 1
            if score == nums[lft] + nums[lft + 1]:
                dfs(lft + 2, rit, score)
            if score == nums[rit] + nums[rit - 1]:
                dfs(lft, rit - 2, score)
            if score == nums[lft] + nums[rit]:
                dfs(lft + 1, rit - 1, score)
            cnt -= 1

        lft, rit = 0, len(nums) - 1
        cnt += 1
        dfs(lft = lft + 2, rit = rit, score = nums[lft] + nums[lft + 1])
        dfs(lft = lft, rit = rit - 2, score = nums[rit] + nums[rit - 1])
        dfs(lft = lft + 1, rit = rit - 1, score = nums[lft] + nums[rit])
        cnt -= 1
        return ans
