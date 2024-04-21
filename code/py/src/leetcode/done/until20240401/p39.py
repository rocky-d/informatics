from rockyutil.leetcode import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        combination = deque()
        n = len(candidates)

        def dfs(vol: int, idx: int) -> None:
            if 0 == vol:
                ans.append(list(combination))
                return
            candidate = candidates[idx]
            if 0 <= vol - candidate:
                combination.append(candidate)
                dfs(vol - candidate, idx)
                combination.pop()
            idx += 1
            if idx < n:
                dfs(vol, idx)

        dfs(vol = target, idx = 0)
        return ans
