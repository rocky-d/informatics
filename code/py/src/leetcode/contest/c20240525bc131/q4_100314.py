from rockyutil.leetcode import *


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        ans = []
        blocks = []
        slots = list(range(1 + min(50_000, 3 * len(queries))))
        for query in queries:
            if 1 == query[0]:
                insort(blocks, query[1])
            else:  # elif 2 == query[0]:
                ans.append(query[2] <= slots[query[1]])
        return ans
