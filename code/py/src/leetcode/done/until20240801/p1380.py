from rockyutil.leetcode import *


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        return [num for i, num in (min(enumerate(row), key = lambda item: item[1]) for row in matrix) if all(row[i] <= num for row in matrix)]
