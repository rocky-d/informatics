from rockyutil.leetcode import *


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        stamp_len, target_len = len(stamp), len(target)
        nodes = target_len - stamp_len + 1
        graph = [[] for _ in range(target_len)]
        ins = [stamp_len for _ in range(nodes)]
        que = deque()
        for i in range(nodes):
            for j in range(stamp_len):
                if stamp[j] == target[i + j]:
                    ins[i] -= 1
                    if 0 == ins[i]:
                        que.append(i)
                else:
                    graph[i + j].append(i)
        order = []
        seen = [False for _ in target]
        while 0 < len(que):
            node = que.popleft()
            order.append(node)
            for i in range(stamp_len):
                if not seen[node + i]:
                    seen[node + i] = True
                    for edge in graph[node + i]:
                        ins[edge] -= 1
                        if ins[edge] == 0:
                            que.append(edge)
        return order[::-1] if nodes == len(order) else []
