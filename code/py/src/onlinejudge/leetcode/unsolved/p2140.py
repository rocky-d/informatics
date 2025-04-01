from onlinejudge.leetcode import *


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [(0, 0)]
        for index, (points, brainpower) in enumerate(questions):
            insort(dp, (index + brainpower + 1, dp[bisect(dp, (index, inf)) - 1][1] + points))
        return max(score for _, score in dp)


eg_questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
print(Solution().mostPoints(eg_questions))
