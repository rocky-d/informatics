from rockyutil.leetcode import *


class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        excludes = set()
        for row in range(m):
            for col in range(1, n):
                if threshold < abs(image[row][col - 1] - image[row][col]):
                    for x, y in ((-2, -2), (-2, -1), (-1, -2), (-1, -1), (0, -2), (0, -1)):
                        excludes.add((row + x, col + y))
        for col in range(n):
            for row in range(1, m):
                if threshold < abs(image[row - 1][col] - image[row][col]):
                    for x, y in ((-2, -2), (-2, -1), (-2, 0), (-1, -2), (-1, -1), (-1, 0)):
                        excludes.add((row + x, col + y))
        pres = [[0 for _ in range(1 + n)]]
        for row in range(m):
            pres.append([0])
            for col in range(n):
                pres[-1].append(image[row][col] + pres[row + 1][col] + pres[row][col + 1] - pres[row][col])
        totals = [[[0, 0] for _ in range(n)] for _ in range(m)]
        for row in range(m - 2):
            for col in range(n - 2):
                if (row, col) in excludes:
                    continue
                average = (pres[row + 3][col + 3] - pres[row + 3][col] - pres[row][col + 3] + pres[row][col]) // 9
                for x, y in ((0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)):
                    totals[row + x][col + y][0] += average
                    totals[row + x][col + y][1] += 1
        return [[image[row][col] if 0 == totals[row][col][1] else totals[row][col][0] // totals[row][col][1] for col in range(n)] for row in range(m)]


eg_image = [
    [5, 6, 7, 10],
    [8, 9, 10, 10],
    [11, 12, 13, 10]
]
eg_threshold = 3
print(Solution().resultGrid(eg_image, eg_threshold))
