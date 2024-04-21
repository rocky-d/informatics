from rockyutil.leetcode import *


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        heads = list(range(n))

        def find(x: int) -> int:
            if x == heads[x]:
                return x
            heads[x] = find(heads[x])
            return heads[x]

        for a, b in edges:
            a_head, b_head = find(x = a), find(x = b)
            if a_head != b_head:
                heads[a] = heads[a_head] = b_head
        return find(x = source) == find(x = destination)
