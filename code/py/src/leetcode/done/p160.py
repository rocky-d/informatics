from rockyutil.leetcode import *


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node1 = headA
        node2 = headB
        while node1 is not node2:
            node1 = headB if node1 is None else node1.next
            node2 = headA if node2 is None else node2.next
        return node1
