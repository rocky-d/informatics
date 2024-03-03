from rockyutil.leetcode import *


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        node1, node2 = dummy, dummy
        for _ in range(1 + n):
            node1 = node1.next
        while node1 is not None:
            node1, node2 = node1.next, node2.next
        node2.next = node2.next.next
        return dummy.next


eg_head = link([1, 2, 3, 4, 5])
eg_n = 2
print(*unlink(Solution().removeNthFromEnd(eg_head, eg_n)))
