from onlinejudge.leetcode import *


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        total = sum(candidates)
        if total < target:
            return []
        if total == target:
            return [candidates]
        ans = []
        groups = list((candidate, len(list(group))) for candidate, group in groupby(sorted(candidates)))
        m = len(groups)
        stk = deque()

        def dfs(idx: int, num: int) -> bool:
            if target == num:
                ans.append(reduce(add, ([candidate] * times for candidate, times in stk)))
                return True
            if target < num:
                return True
            if idx == m:
                return False
            candidate, times = groups[idx]
            stk.append([candidate, 0])
            idx += 1
            for _ in range(1 + times):
                if dfs(idx, num):
                    break
                num += candidate
                stk[-1][1] += 1
            stk.pop()
            return False

        dfs(idx = 0, num = 0)
        return ans


eg_candidates = [10, 1, 2, 7, 6, 1, 5]
eg_target = 8
print(Solution().combinationSum2(eg_candidates, eg_target))
