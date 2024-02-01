from rockyutil.leetcode import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations_set = set()

        def dfs(last: int, combinations: Dict[int, int]) -> None:
            if last < 0:
                return
            if 0 == last:
                combinations_set.add(tuple(combinations.items()))
                return
            for candidate in candidates:
                combinations[candidate] += 1
                dfs(last = last - candidate, combinations = combinations)
                combinations[candidate] -= 1

        dfs(last = target, combinations = {candidate: 0 for candidate in candidates})
        return [reduce(lambda x, y: x + y, [[num for _ in range(cnt)] for num, cnt in combination]) for combination in combinations_set]
