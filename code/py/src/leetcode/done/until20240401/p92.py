from rockyutil.leetcode import *


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        lft = dummy
        for _ in range(left - 1):
            lft = lft.next
        start = lft.next
        node = start
        stk = deque([node])
        for _ in range(left, right):
            node = node.next
            stk.append(node)
        lft.next = node
        rit = node.next
        for _ in range(1, len(stk)):
            node = stk.pop()
            node.next = stk[-1]
        start.next = rit
        return dummy.next
