from onlinejudge.leetcode import *


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        ans = 0
        idxes = [None] + [[] for _ in range(1, 101)]
        for idx, row in enumerate(grid):
            for num in row:
                idxes[num].append(idx)
        stk = deque()

        @lru_cache(maxsize=None)
        def dfs(num: int, vis: int) -> None:
            nonlocal ans
            if num == 101:
                ans = max(ans, sum(stk))
                return
            dfs(num + 1, vis)
            for idx in idxes[num]:
                if 0b1 == 0b1 & (vis >> idx):
                    continue
                stk.append(num)
                dfs(num + 1, vis | (0b1 << idx))
                stk.pop()

        dfs(num=1, vis=0b0)
        return ans


eg_grid = [
    [5],
    [7],
    [19],
    [5],
]
print(Solution().maxScore(eg_grid))
