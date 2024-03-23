from rockyutil.leetcode import *


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dque1, dque2 = deque(), deque()
        node = head
        while node is not None:
            dque1.append(node)
            node = node.next
        for _ in range(len(dque1) // 2):
            dque2.append(dque1.pop())
        dummy = ListNode()
        node = dummy
        for node1, node2 in zip(dque1, dque2):
            node.next = node1
            node = node.next
            node.next = node2
            node = node.next
        if len(dque1) == len(dque2) + 1:
            node.next = dque1[-1]
            node = node.next
        node.next = None
        return dummy.next
