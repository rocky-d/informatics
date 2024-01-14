from rockyutil.leetcode import *


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode(val = 101, next = head)
        while node is not None:
            while node.next is not None and node.val == node.next.val:
                node.next = node.next.next
            node = node.next
        return dummy.next
