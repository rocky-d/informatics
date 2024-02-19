from rockyutil.leetcode import *


class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        @cache
        def is_prime(num: int):
            return all(num % i for i in range(2, isqrt(num) + 1))

        cnter = Counter()
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                for ofst_x, ofst_y in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
                    num = mat[i][j]
                    x, y = i + ofst_x, j + ofst_y
                    while 0 <= x < m and 0 <= y < n:
                        num = 10 * num + mat[x][y]
                        if is_prime(num = num):
                            cnter[num] += 1
                        x += ofst_x
                        y += ofst_y
        return -1 if 0 == len(cnter) else max(cnter.items(), key = lambda item: (item[1], item[0]))[0]
