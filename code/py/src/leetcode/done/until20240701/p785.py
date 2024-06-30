from rockyutil.leetcode import *


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        parts = [0 for _ in graph]

        def dfs(node: int, is_part1: bool) -> bool:
            parts[node] = 1 if is_part1 else 2
            is_part1_nxt = not is_part1
            for nxt in graph[node]:
                if 1 == parts[nxt]:
                    if not is_part1_nxt:
                        res = True
                        break
                elif 2 == parts[nxt]:
                    if is_part1_nxt:
                        res = True
                        break
                else:
                    if dfs(nxt, is_part1_nxt):
                        res = True
                        break
            else:
                res = False
            return res

        return not any(dfs(node = node, is_part1 = True) for node in range(len(graph)) if 0 == parts[node])
