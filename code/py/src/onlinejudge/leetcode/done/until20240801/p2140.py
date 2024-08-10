from onlinejudge.leetcode import *


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [questions.pop(-1)[0]]
        for point, brainpower in reversed(questions):
            dp.insert(0, max(dp[0], point + dp[brainpower] if brainpower < len(dp) else point))
        return dp[0]


eg_questions = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
print(Solution().mostPoints(eg_questions))
