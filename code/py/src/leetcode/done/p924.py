from rockyutil.leetcode import *


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        heads = [node for node in range(n)]
        groups = {node: {node} for node in range(n)}

        def find(node: int) -> int:
            if node == heads[node]:
                return node
            heads[node] = find(heads[node])
            return heads[node]

        for a, row in enumerate(graph):
            for b in range(a + 1, n):
                if 1 == row[b]:
                    a_head, b_head = find(node = a), find(node = b)
                    if a_head != b_head:
                        heads[a] = heads[a_head] = b_head
                        groups[b_head] |= groups.pop(a_head)
        owns = defaultdict(lambda: [])
        for head, group in groups.items():
            for init in initial:
                if init in group:
                    owns[head].append(init)
        cans = sorted((-len(groups[head]), inits[0]) for head, inits in owns.items() if 1 == len(inits))
        return min(initial) if 0 == len(cans) else cans[0][1]


eg_graph = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 1],
]
eg_initial = [3, 1]
print(Solution().minMalwareSpread(eg_graph, eg_initial))
