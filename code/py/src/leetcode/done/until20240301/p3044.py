from rockyutil.leetcode import *


class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        @cache
        def is_prime(num: int):
            return all(0 != num % divisor for divisor in range(2, isqrt(num) + 1))

        cnter = Counter()
        m, n = len(mat), len(mat[0])
        for row in range(m):
            for col in range(n):
                for oft_x, oft_y in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
                    x, y = row + oft_x, col + oft_y
                    num = mat[row][col]
                    while 0 <= x < m and 0 <= y < n:
                        num = 10 * num + mat[x][y]
                        if is_prime(num = num):
                            cnter[num] += 1
                        x += oft_x
                        y += oft_y
        return -1 if 0 == len(cnter) else max(cnter.items(), key = lambda item: (item[1], item[0]))[0]
