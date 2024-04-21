from rockyutil.leetcode import *


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        combination = deque()

        def dfs(vol: int, fr: int) -> None:
            if 0 == vol:
                if k == len(combination):
                    ans.append(list(combination))
                return
            for num in range(fr, 10):
                if 0 <= vol - num:
                    combination.append(num)
                    dfs(vol - num, num + 1)
                    combination.pop()
                else:
                    break

        dfs(vol = n, fr = 1)
        return ans
