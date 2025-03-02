from onlinejudge.leetcode import *


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        idxes = []
        node, idx = head, 0
        while node.next.next is not None:
            nxt = node.next
            if nxt.val < node.val and nxt.val < nxt.next.val or nxt.val > node.val and nxt.val > nxt.next.val:
                idxes.append(idx)
            idx += 1
            node = nxt
        return [-1, -1] if len(idxes) < 2 else [min(nxt - lst for lst, nxt in pairwise(idxes)), idxes[-1] - idxes[0]]
