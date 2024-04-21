from rockyutil.leetcode import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        combination = deque()
        n = len(candidates)

        def dfs(idx: int, vol: int) -> None:
            if 0 == vol:
                ans.append(list(combination))
                return
            candidate = candidates[idx]
            if 0 <= vol - candidate:
                combination.append(candidate)
                dfs(idx, vol - candidate)
                combination.pop()
            idx += 1
            if idx < n:
                dfs(idx, vol)

        dfs(idx = 0, vol = target)
        return ans
