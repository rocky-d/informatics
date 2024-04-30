from rockyutil.leetcode import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        combo = deque()
        candidates.sort()
        n = len(candidates)

        def dfs(vol: int, idx: int) -> None:
            if 0 == vol:
                ans.append(list(combo))
                return
            for i in range(idx, n):
                candidate = candidates[i]
                if 0 <= vol - candidate:
                    combo.append(candidate)
                    dfs(vol - candidate, i)
                    combo.pop()
                else:
                    break

        dfs(vol = target, idx = 0)
        return ans
