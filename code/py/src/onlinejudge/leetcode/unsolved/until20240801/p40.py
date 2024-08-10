from onlinejudge.leetcode import *


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = set()

        def dfs(last: int, comb: Dict[int, int], cand: Set[int]) -> None:
            if last < 0:
                return
            if 0 == last:
                combinations.add(tuple(comb.items()))
                return
            for i in cand:
                comb[candidates[i]] += 1
                dfs(last = last - candidates[i], comb = comb, cand = cand - {i})
                comb[candidates[i]] -= 1

        dfs(last = target, comb = {candidate: 0 for candidate in candidates}, cand = set(i for i in range(len(candidates))))
        return [reduce(lambda x, y: x + y, [[num for _ in range(cnt)] for num, cnt in combination]) for combination in combinations]
