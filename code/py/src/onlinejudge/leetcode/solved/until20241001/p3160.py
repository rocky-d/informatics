from onlinejudge.leetcode import *


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ans = []
        colors = Counter()
        balls = {}
        for idx, color in queries:
            if idx not in balls.keys():
                balls[idx] = color
                colors[color] += 1
            elif balls[idx] != color:
                colors[balls[idx]] -= 1
                if 0 == colors[balls[idx]]:
                    colors.pop(balls[idx])
                balls[idx] = color
                colors[color] += 1
            ans.append(len(colors))
        return ans
