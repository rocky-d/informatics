from onlinejudge.leetcode import *


class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        def primes_before_eratosthenes(n: int) -> Iterable[int]:
            tags = [False for _ in range(min(2, n))] + [True for _ in range(2, n)]
            for num in range(2, n):
                if tags[num]:
                    yield num
                    for composite in range(num * num, n, num):
                        tags[composite] = False

        m, n = len(mat), len(mat[0])
        primes = frozenset(primes_before_eratosthenes(n = 10 ** max(m, n)))
        cnter = Counter()
        for i in range(m):
            for j in range(n):
                for x, y in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                    num = mat[i][j]
                    a, b = i + x, j + y
                    while 0 <= a < m and 0 <= b < n:
                        num = 10 * num + mat[a][b]
                        if num in primes:
                            cnter[num] += 1
                        a += x
                        b += y
        return -1 if 0 == len(cnter) else max(cnter.items(), key = lambda item: (item[1], item[0]))[0]


eg_mat = [
    [7, 1, 2, 4, 6, 7],
    [3, 4, 6, 2, 7, 9],
    [1, 3, 0, 3, 4, 8],
    [9, 0, 3, 2, 5, 7],
    [1, 4, 7, 9, 4, 3],
    [1, 3, 6, 1, 7, 4],
]
print(Solution().mostFrequentPrime(eg_mat))
