from rockyutil.leetcode import *


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ans = 0
        cost.insert(0, 0)

        def dfs(node: int) -> int:
            nonlocal ans
            if n < node:
                return 0
            node_double = node + node
            lft, rit = dfs(node = node_double), dfs(node = node_double + 1)
            ans += abs(lft - rit)
            return max(lft, rit) + cost[node]

        dfs(node = 1)
        return ans
