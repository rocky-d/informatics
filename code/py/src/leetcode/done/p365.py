class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        seen = set()

        def dfs(jug1, jug2) -> bool:
            if (jug1, jug2) in seen:
                return False
            seen.add((jug1, jug2))
            if targetCapacity in (jug1, jug2, jug1 + jug2):
                res = True
            elif dfs(jug1 = 0, jug2 = jug2):
                res = True
            elif dfs(jug1 = jug1, jug2 = 0):
                res = True
            elif dfs(jug1 = jug1Capacity, jug2 = jug2):
                res = True
            elif dfs(jug1 = jug1, jug2 = jug2Capacity):
                res = True
            elif dfs(jug1 = jug1 - min(jug1, jug2Capacity - jug2), jug2 = jug2 + min(jug1, jug2Capacity - jug2)):
                res = True
            elif dfs(jug1 = jug1 + min(jug2, jug1Capacity - jug1), jug2 = jug2 - min(jug2, jug1Capacity - jug1)):
                res = True
            else:
                res = False
            return res

        return dfs(jug1 = 0, jug2 = 0)
