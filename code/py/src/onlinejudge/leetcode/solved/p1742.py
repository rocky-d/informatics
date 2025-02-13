from onlinejudge.leetcode import *


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = defaultdict(lambda: 0)
        for ball in range(lowLimit, highLimit + 1):
            boxes[sum(map(int, str(ball)))] += 1
        return max(boxes.values())
