from onlinejudge.leetcode import *


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        end = ListNode(next = head)
        nodes = 0
        while end.next is not None:
            end = end.next
            nodes += 1
        if 0 == nodes:
            return None
        k %= nodes
        if 0 == k:
            return head
        fast, slow = head, head
        for _ in range(k):
            fast = fast.next
        while fast.next is not None:
            fast, slow = fast.next, slow.next
        ans, slow.next = slow.next, None
        end.next = head
        return ans
