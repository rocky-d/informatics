from rockyutil.leetcode import *


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        combo = deque()

        def dfs(vol: int, fr: int) -> None:
            if k == len(combo) or 0 == vol:
                if k == len(combo) and 0 == vol:
                    ans.append(list(combo))
                return
            for num in range(fr, 10):
                if 0 <= vol - num:
                    combo.append(num)
                    dfs(vol - num, num + 1)
                    combo.pop()
                else:
                    break

        dfs(vol = n, fr = 1)
        return ans
