import math

from rockyutil.leetcode import *


class Solution:
    ans = 0

    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        ls = [[-1]]
        for road in roads:
            while len(ls) <= road[0]:
                ls.append([])
            ls[road[0]].append(road[1])
            while len(ls) <= road[1]:
                ls.append([])
            ls[road[1]].append(road[0])

        def dfs(node: int, parent: int) -> int:
            if 1 == len(ls[node]):
                members = 1
                self.ans += math.ceil(members / seats)
                return members
            members = 1
            for child in ls[node]:
                if child == parent:
                    continue
                members += dfs(child, node)
            self.ans += math.ceil(members / seats)
            return members

        last = dfs(0, -1)
        return self.ans - math.ceil(last / seats)


sol = Solution()

eg_roads = [[0, 1], [1, 2]]
eg_seats = 3
print(sol.minimumFuelCost(roads = eg_roads, seats = eg_seats))
