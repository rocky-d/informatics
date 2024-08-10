from onlinejudge.leetcode import *


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        distances = []
        for i in range(n):
            distances.append([0])
            counter = defaultdict(lambda: 0)
            for j in range(i):
                counter[distances[j][i - j]] += 1
            for j in range(i + 1, n):
                distances[-1].append((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
                counter[distances[-1][-1]] += 1
            for count in counter.values():
                ans += count * (count - 1)
        return ans
