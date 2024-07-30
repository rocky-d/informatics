from rockyutil.leetcode import *


class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        return [i for i, (a, b, c, m) in enumerate(variables) if target == pow(pow(a, b) % 10, c) % m]
