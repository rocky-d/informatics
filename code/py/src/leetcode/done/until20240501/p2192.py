from rockyutil.leetcode import *


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = [set() for _ in range(n)]
        graph = [[] for _ in range(n)]
        ins = [0 for _ in range(n)]
        for fr, to in edges:
            graph[fr].append(to)
            ins[to] += 1
        que = deque([idx for idx, val in enumerate(ins) if 0 == val])
        while 0 < len(que):
            node = que.popleft()
            for nxt in graph[node]:
                ancestors[nxt].add(node)
                ancestors[nxt] |= ancestors[node]
                ins[nxt] -= 1
                if 0 == ins[nxt]:
                    que.append(nxt)
        return [sorted(val) for val in ancestors]
