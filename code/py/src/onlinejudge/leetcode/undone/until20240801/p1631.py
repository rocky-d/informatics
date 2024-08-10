from onlinejudge.leetcode import *


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, columns = len(heights), len(heights[0])
        queue = [(0, 0, 0)]
        dist = [int(1e6) for _ in range(rows * columns)]
        dist[0] = 0
        seen = set()

        while queue:
            d, x, y = heapq.heappop(queue)
            if (x, y) in seen:
                continue
            if (x, y) == (rows - 1, columns - 1):
                break
            seen.add((x, y))
            for next_x, next_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if -1 < next_x < rows and -1 < next_y < columns and max(d, abs(heights[x][y] - heights[next_x][next_y])) <= dist[next_x * columns + next_y]:
                    dist[next_x * columns + next_y] = max(d, abs(heights[x][y] - heights[next_x][next_y]))
                    heapq.heappush(queue, (dist[next_x * columns + next_y], next_x, next_y))
        return dist[rows * columns - 1]


eg_heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]

print(Solution().minimumEffortPath(heights = eg_heights))
