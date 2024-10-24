from onlinejudge.leetcode import *


class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        if n <= k:
            return max(range(n), key=lambda idx: skills[idx])
        ans = 0
        maxm, cnt = skills.pop(0), 0
        for idx, skill in enumerate(skills, start=1):
            if maxm < skill:
                maxm = skill
                ans = idx
                cnt = 0
            cnt += 1
            if k == cnt:
                break
        return ans
