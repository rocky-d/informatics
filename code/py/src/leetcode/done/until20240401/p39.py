from rockyutil.leetcode import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = set()

        def dfs(last: int, combination: Dict[int, int]) -> None:
            if last < 0:
                return
            if 0 == last:
                combinations.add(tuple(combination.items()))
                return
            for candidate in candidates:
                combination[candidate] += 1
                dfs(last = last - candidate, combination = combination)
                combination[candidate] -= 1

        dfs(last = target, combination = {candidate: 0 for candidate in candidates})
        return [reduce(lambda x, y: x + y, [[num for _ in range(cnt)] for num, cnt in combination]) for combination in combinations]
