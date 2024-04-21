from rockyutil.leetcode import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        combination = deque()
        candidates.sort()
        n = len(candidates)

        def dfs(vol: int, idx: int) -> None:
            if 0 == vol:
                ans.append(list(combination))
                return
            for i in range(idx, n):
                candidate = candidates[i]
                if 0 <= vol - candidate:
                    combination.append(candidate)
                    dfs(vol - candidate, i)
                    combination.pop()
                else:
                    break

        dfs(vol = target, idx = 0)
        return ans
