from onlinejudge.leetcode import *


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        node = head
        while node is not None:
            node = node.next
            n += 1
        node = dummy = ListNode(next = head)
        for _ in range(n // 2):
            node = node.next
        node.next = node.next.next
        return dummy.next
