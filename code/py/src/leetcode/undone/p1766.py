from rockyutil.leetcode import *


class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        ans = [-1 for _ in nums]
        valid_pairs = set((i, j) for i in range(1, 51) for j in range(i, 51) if 1 == gcd(i, j))
        graph = [[] for _ in nums]
        for u, v in edges:
            graph[u].append(v), graph[v].append(u)
        ancestors = deque()

        def dfs(node: int, lst: int) -> None:
            for ancestor in ancestors:
                pair = (nums[node], nums[ancestor]) if nums[node] < nums[ancestor] else (nums[ancestor], nums[node])
                if pair in valid_pairs:
                    ans[node] = ancestor
                    break
            ancestors.appendleft(node)
            for nxt in graph[node]:
                if lst != nxt:
                    dfs(nxt, node)
            ancestors.popleft()

        dfs(node = 0, lst = -1)
        return ans


eg_nums = [2, 3, 3, 2]
eg_edges = [[0, 1], [1, 2], [1, 3]]
print(Solution().getCoprimes(eg_nums, eg_edges))
