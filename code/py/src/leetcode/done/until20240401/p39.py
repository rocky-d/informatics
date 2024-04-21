from rockyutil.leetcode import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        combination = []
        n = len(candidates)

        def dfs(idx: int, vol: int) -> None:
            if 0 == vol:
                ans.append(combination.copy())
                return
            if idx + 1 < n:
                dfs(idx + 1, vol)
            candidate = candidates[idx]
            if 0 <= vol - candidate:
                combination.append(candidate)
                dfs(idx, vol - candidate)
                combination.pop(-1)

        dfs(idx = 0, vol = target)
        return ans
