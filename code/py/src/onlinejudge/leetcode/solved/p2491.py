from onlinejudge.leetcode import *


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total = sum(skill)
        if 0 != total % (len(skill) // 2):
            return -1
        ans = 0
        pair = total // (len(skill) // 2)
        idxes = [None] + [deque() for _ in range(max(skill))]
        for idx, val in enumerate(skill):
            idxes[val].append(idx)
        vis = [False] * len(skill)
        for i in range(len(skill)):
            if vis[i]:
                continue
            vis[i] = True
            for _ in range(len(idxes[pair - skill[i]])):
                idx = idxes[pair - skill[i]].popleft()
                if vis[idx]:
                    continue
                vis[idx] = True
                ans += skill[i] * skill[idx]
                break
            else:
                ans = -1
                break
        return ans
