from rockyutil.leetcode import *


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        seen1, seen2 = set(), set()

        def dfs(node: int, is_set1: bool) -> bool:
            if is_set1:
                seen1.add(node)
            else:
                seen2.add(node)
            for nxt in graph[node]:
                if nxt in seen1:
                    if is_set1:
                        res = True
                        break
                elif nxt in seen2:
                    if not is_set1:
                        res = True
                        break
                else:
                    if dfs(nxt, not is_set1):
                        res = True
                        break
            else:
                res = False
            return res

        return not any(dfs(node = i, is_set1 = True) for i in range(len(graph)) if i not in seen1 and i not in seen2)
